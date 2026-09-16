<!-- Mirrored from https://docs.smartlyq.com. The docs are the source of truth;
     if this file and the docs disagree, the docs win. -->

# Errors

> Error codes, response format, and troubleshooting.

## Error response format

All errors follow a consistent JSON structure:

```json
{
  "success": false,
  "error": {
    "code": "ERROR_CODE",
    "message": "Human-readable description."
  }
}
```

## HTTP status codes

| Code  | Meaning                                      |
| ----- | -------------------------------------------- |
| `200` | Success                                      |
| `201` | Created                                      |
| `202` | Accepted (async job queued)                  |
| `204` | No Content (resource deleted)                |
| `400` | Bad Request — invalid parameters             |
| `401` | Unauthorized — missing or invalid API key    |
| `402` | Payment Required — insufficient credits      |
| `403` | Forbidden — valid key but insufficient scope |
| `404` | Not Found — resource does not exist          |
| `409` | Conflict — duplicate request (idempotency)   |
| `422` | Unprocessable Entity — validation error      |
| `429` | Too Many Requests — rate limited             |
| `500` | Internal Server Error                        |

## Common error codes

| Code                           | Description                                                                                                                                                                                                                                                                                                                                |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `UNAUTHORIZED`                 | API key is missing or invalid                                                                                                                                                                                                                                                                                                              |
| `FORBIDDEN`                    | Key lacks the required scope                                                                                                                                                                                                                                                                                                               |
| `CONNECTION_SCOPE_MISSING`     | The connected social account is missing a permission this call needs, usually because it was connected before SmartlyQ requested that permission. Reconnect the account to fix it; `details.reconnect_required` is `true`.                                                                                                                 |
| `INSUFFICIENT_CREDITS`         | Wallet balance too low                                                                                                                                                                                                                                                                                                                     |
| `RATE_LIMITED`                 | Too many requests                                                                                                                                                                                                                                                                                                                          |
| `VALIDATION_ERROR`             | Request body failed validation                                                                                                                                                                                                                                                                                                             |
| `RESOURCE_NOT_FOUND`           | The requested resource does not exist                                                                                                                                                                                                                                                                                                      |
| `IDEMPOTENCY_CONFLICT`         | A request with this idempotency key was already processed                                                                                                                                                                                                                                                                                  |
| `MODEL_NOT_AVAILABLE`          | The requested AI model is not available on your plan                                                                                                                                                                                                                                                                                       |
| `JOB_FAILED`                   | An async job encountered an error                                                                                                                                                                                                                                                                                                          |
| `POST_TYPE_UNSUPPORTED`        | `platform_options.<platform>.type` names a post format this platform cannot publish. The message lists the accepted values; see [Platform options](/guides/platform-options).                                                                                                                                                              |
| `PLATFORM_DAILY_LIMIT_REACHED` | HTTP `422`, not retryable. The platform's daily limit for this post type is used up for a selected account - today, Facebook's 30 Reels per Page in a moving 24-hour window. Nothing is created. Publish after `details.next_available_at`, or send the post as a different type. `details` also carries `account_id`, `limit` and `used`. |

## Idempotency

For POST requests, include an `X-Idempotency-Key` header to prevent duplicate operations:

```bash
curl -X POST https://api.smartlyq.com/v1/articles/generate \
  -H "Authorization: Bearer sqk_live_xxxxxxxxxxxx" \
  -H "X-Idempotency-Key: unique-request-id-123" \
  -H "Content-Type: application/json" \
  -d '{ "topic": "My Article", "language": "en" }'
```

Idempotency keys expire after **24 hours**.
