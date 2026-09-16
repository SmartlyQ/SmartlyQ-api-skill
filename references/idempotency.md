<!-- Mirrored from https://docs.smartlyq.com. The docs are the source of truth;
     if this file and the docs disagree, the docs win. -->

# Idempotency & Safe Retries

> Retry any create call without ever double-posting.

Network timeouts, 5xx responses, and dropped connections leave you not knowing whether a `POST /v1/social/posts` landed. SmartlyQ has two independent layers so a retry is always safe.

## Layer 1: idempotency keys

Send an `X-Idempotency-Key` header (`X-Request-Id` is accepted as an alias) with a fresh value per **logical** post - generate a UUID v4 in your code. If the call fails ambiguously (timeout, 5xx, connection reset), retry it with the **same** key:

```bash
curl -X POST https://api.smartlyq.com/v1/social/posts \
  -H "Authorization: Bearer sqk_live_xxxxxxxxxxxx" \
  -H "X-Idempotency-Key: YOUR-UNIQUE-KEY-PER-POST" \
  -H "Content-Type: application/json" \
  -d '{ "content": "Launch day!", "platforms": ["twitter"], "account_ids": [123] }'
```

* **First call** creates the post and returns `201`.
* **A retry with the same key** returns `200` with the original post and `idempotent_replay: true` - nothing new is created:

```json Replay response (200)
{
  "success": true,
  "data": { "post_id": 8841, "status": "published", "idempotent_replay": true }
}
```

Keys are scoped to your workspace, up to 64 characters (`A-Z a-z 0-9 . _ : -`), and permanently identify their post - there is no expiry window to race against. Deleting the post frees its key. Concurrent retries are safe: a unique database constraint guarantees only one post can ever own a key.

Works on `POST /social/posts` and `POST /social/posts/schedule` (including queue scheduling).

## Layer 2: duplicate-content guard

Independent of headers, creating **identical content** in the same workspace within **24 hours** returns `409 DUPLICATE_CONTENT` with the existing post's id:

```json 409 response
{
  "success": false,
  "error": {
    "code": "DUPLICATE_CONTENT",
    "message": "Identical content was already posted in this workspace within the last 24 hours (post 8841). Pass allow_duplicates: true to post it anyway.",
    "details": { "existing_post_id": 8841 }
  }
}
```

This catches the classic mis-wired-cron bug even when no idempotency key was sent. Intentional re-posts opt out per request with `"allow_duplicates": true` in the body. Posts that ended `failed` or were unpublished never block a re-post.

## How the layers interact

1. Same idempotency key seen before → **200 replay** of the original post (wins over the duplicate guard - a retry is not a duplicate).
2. No (or new) key, identical content within 24h → **409 DUPLICATE\_CONTENT**.
3. Otherwise → the post is created normally.

## Retry rules of thumb

| You got                              | Do                                                                            |
| ------------------------------------ | ----------------------------------------------------------------------------- |
| Timeout / connection reset / 5xx     | Retry with the **same** `X-Idempotency-Key`                                   |
| `200` with `idempotent_replay: true` | Treat as success - the original post's id is in `post_id`                     |
| `409 DUPLICATE_CONTENT`              | You (or another process) already posted this - use `details.existing_post_id` |
| `429`                                | Back off per `Retry-After`, then retry with the same key                      |
| `422` validation errors              | Fix the request - do not blind-retry                                          |
