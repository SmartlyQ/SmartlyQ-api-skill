<!-- Mirrored from https://docs.smartlyq.com. The docs are the source of truth;
     if this file and the docs disagree, the docs win. -->

# Webhooks

> Receive real-time notifications when events happen.

## Overview

Webhooks let your server receive HTTP POST callbacks when events occur in SmartlyQ - a post publishing, a new comment or DM arriving, a contact being created, your wallet running low, and more. There are **38 events** across posting, accounts, inbox, reviews, jobs, billing, and CRM.

## Setting up webhooks

Two ways to register an endpoint (both HTTPS-only, public URLs):

* **Dashboard**: [Developer Dashboard](https://app.smartlyq.com/next/developer) → **Webhooks** tab → add an endpoint URL and select events.
* **API**: `POST /webhooks` with `url` and an `events` array (see the [API reference](/api-reference/webhooks/create-webhook)). The response includes the signing `secret` - shown exactly once.

The full management surface via API: list (`GET /webhooks`), create (`POST /webhooks`), update url/events or pause/resume (`PUT /webhooks/{id}`), send a signed test delivery (`POST /webhooks/{id}/test`), inspect the delivery log (`GET /webhooks/logs`), and delete (`DELETE /webhooks/{id}`).

Limits and safety: up to **10 active webhooks per workspace**; URLs must be public HTTPS endpoints (internal/private addresses are rejected at save time and re-checked at delivery time); unknown event names are rejected with a validation error. Webhooks are a developer-workspace resource: the `X-Profile-Id` header is not accepted on webhook routes - profile events reach your webhooks automatically via fan-up.

<Tip>
  `POST /webhooks/{id}/test` sends a `webhook.test` event through the real signing pipeline (same headers, same HMAC) and returns the outcome synchronously - the fastest way to verify your endpoint and signature code. Test deliveries are never retried.
</Tip>

## Delivery envelope

Every delivery is JSON with the same envelope:

```json
{
  "id": "evt_9f2c1a7d3b4e5f60718293a4",
  "event": "post.published",
  "created_at": "2026-07-26T14:30:00Z",
  "data": {
    "post_id": 12345,
    "status": "published",
    "platforms": [
      { "platform": "instagram", "success": true },
      { "platform": "twitter", "success": true }
    ]
  }
}
```

* `id` is a **stable event identifier**: it is shared across fan-out to multiple endpoints and reused on every retry of the same delivery, so you can deduplicate at-least-once delivery. It is also echoed in the `X-SmartlyQ-Event-Id` header so you can dedupe without parsing the body.
* `created_at` is UTC, ISO 8601.
* `data` is the event-specific payload (catalog below).

<Note>
  **Profiles fan-up:** if you use [Profiles](/guides/profiles) (sub-accounts for your end customers), events raised inside a profile's workspace are also delivered to **your** webhooks, with two extra fields added to `data`: `profile_id` and `profile_workspace_id`, so you can attribute the event to the right end customer.
</Note>

## Headers

| Header                 | Value                                         |
| ---------------------- | --------------------------------------------- |
| `Content-Type`         | `application/json`                            |
| `X-SmartlyQ-Signature` | `t=<timestamp>,v1=<hmac>` (see below)         |
| `X-SmartlyQ-Event`     | The event name, e.g. `post.published`         |
| `X-SmartlyQ-Event-Id`  | The envelope's stable `id`, for deduplication |
| `User-Agent`           | `SmartlyQ-Webhook/1.0`                        |

## Verifying signatures

`X-SmartlyQ-Signature` carries `t=<timestamp>,v1=<hmac>`, where `<hmac>` is the HMAC-SHA256 of `<timestamp>.<raw-body>` keyed with your webhook secret. The timestamp rotates on every attempt; the body (and `id`) stay the same.

```javascript
const crypto = require("crypto");

// rawBody = the exact bytes of the request body (do not re-serialize the JSON)
function verifySignature(rawBody, signatureHeader, secret) {
  const parts = Object.fromEntries(
    signatureHeader.split(",").map((kv) => kv.split("="))
  );
  const expected = crypto
    .createHmac("sha256", secret)
    .update(`${parts.t}.${rawBody}`)
    .digest("hex");
  return crypto.timingSafeEqual(
    Buffer.from(parts.v1),
    Buffer.from(expected)
  );
}
```

<Warning>
  Always verify the signature before processing a webhook. Unverified payloads may be spoofed. The signing secret is shown once, when you create the endpoint.
</Warning>

## Retry policy

* Non-2xx responses are retried up to **5 attempts** with exponential backoff (≈2, 4, 8, 16, 32 minutes).
* If your endpoint answers `429` with a `Retry-After` header, we honor it (capped at 1 hour) instead of the standard backoff.
* After the final attempt the delivery is marked **dead-letter** (it is not silently dropped - you can re-run it from the dashboard Logs).
* **10 consecutive failures** flip the endpoint to `failing` and pause deliveries until you fix and re-enable it.
* Delivery records are retained for **90 days**.

## Event catalog

All registerable events. Registering an event name outside this catalog is rejected with a validation error.

### Posting

| Event                   | Fires when                                                                                | `data` fields                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ----------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `post.published`        | Every platform target published                                                           | `post_id`, `status`, `platforms[]` (`platform`, `success`; on failures `error` `{code, message, retryable}` plus, when the failure came from SmartlyQ's own pre-publish checks, `error.detail` with the exact human-readable reason, e.g. `"Twitter/X caption is 312 characters; the limit is 280. Trim 32 characters and retry."`; when media was auto-fixed before publishing, `transcoded[]` lists what was converted, e.g. `"Video was vp9/webm; converted to H.264/AAC MP4."`) |
| `post.partial`          | Some platforms published, some failed                                                     | same as `post.published`                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `post.failed`           | Every platform target failed                                                              | same as `post.published`                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `post.scheduled`        | A post was accepted and queued for a future publish                                       | `post_id`, `status`, `scheduled_at`, `platforms[]`                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `post.cancelled`        | A scheduled post was cancelled before publishing                                          | `post_id`, `status`                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `post.recycled`         | A recycling chain spawned a new occurrence of a post                                      | `post_id` (the new occurrence), `recycled_from`, `status`, `scheduled_at`                                                                                                                                                                                                                                                                                                                                                                                                           |
| `post.external.created` | A post authored natively on the platform (not via SmartlyQ) was detected by external sync | `post_id`, `platform`, `remote_id`, `status` (`external`)                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `post.external.updated` | A synced native post's text or media changed on the platform                              | same as `post.external.created`                                                                                                                                                                                                                                                                                                                                                                                                                                                     |

### Accounts

| Event                   | Fires when                                       | `data` fields                                                |
| ----------------------- | ------------------------------------------------ | ------------------------------------------------------------ |
| `account.connected`     | A social account is connected or reactivated     | `account_id`, `platform`, `account_name`, `account_username` |
| `account.disconnected`  | An account's connection was revoked/invalidated  | `account_id`, `platform`, `account_name`, `reason`           |
| `account.token_expired` | An account's token expired (reconnect to resume) | `account_id`, `platform`, `account_name`, `reason`           |

### Inbox

| Event                  | Fires when                                                    | `data` fields                                                                                                                                                     |
| ---------------------- | ------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `comment.received`     | A new comment is ingested on one of your posts                | `platform`, `account_id`, `social_post_id` (null for external posts), `remote_post_id`, `remote_comment_id`, `author_name`, `content`, `is_reply`, `commented_at` |
| `message.received`     | A new incoming DM is ingested                                 | `platform`, `account_name`, `conversation_id`, `message_id`, `remote_message_id`, `sender_name`, `content`, `sent_at`                                             |
| `message.sent`         | An outbound DM was delivered from the inbox (via app or API)  | `platform`, `conversation_id`, `message_id`, `remote_message_id`, `content`                                                                                       |
| `conversation.started` | A new inbox conversation was opened with a contact            | `platform`, `conversation_id`, `participant_name`                                                                                                                 |
| `reaction.received`    | A participant added or removed an emoji reaction on a message | `platform`, `action` (`added`/`removed`), `emoji`, `conversation_id`, `message_id`, `remote_message_id`                                                           |
| `message.delivered`    | An outbound message reached the recipient (WhatsApp)          | `platform`, `remote_message_id`, `status`                                                                                                                         |
| `message.read`         | The recipient opened an outbound message (WhatsApp)           | `platform`, `remote_message_id`, `status`                                                                                                                         |
| `message.failed`       | An outbound message failed to deliver (WhatsApp)              | `platform`, `remote_message_id`, `status`, `error` `{code, title, message}`                                                                                       |

### Reviews

| Event            | Fires when                                                       | `data` fields                                                                           |
| ---------------- | ---------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `review.new`     | A new review was posted on a connected account (Google Business) | `review_id`, `account_id`, `platform`, `rating`, `author_name`, `content`, `created_at` |
| `review.updated` | A review was edited, or you posted/removed a reply               | same as `review.new`, plus `reply` when present                                         |

### Jobs

| Event           | Fires when                         | `data` fields                       |
| --------------- | ---------------------------------- | ----------------------------------- |
| `job.completed` | An async job finished successfully | `job_id`, `type`, `status`          |
| `job.failed`    | An async job failed                | `job_id`, `type`, `status`, `error` |

### Billing & keys

| Event                       | Fires when                                              | `data` fields                                                                                                                      |
| --------------------------- | ------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| `balance.low`               | Wallet balance crossed below the low threshold          | `balance`, `threshold`                                                                                                             |
| `balance.depleted`          | Wallet balance reached zero                             | `balance`                                                                                                                          |
| `key.revoked`               | An API key was revoked                                  | `key_id`, `key_prefix`, `name`                                                                                                     |
| `wallet.recharge.succeeded` | Auto-recharge charged your card and credited the wallet | `amount`, `currency`, `balance_after`                                                                                              |
| `wallet.recharge.failed`    | Auto-recharge failed (or grace expired)                 | `amount`, `currency`, `error`, `balance`, `retry_after`; on grace-expiry pauses instead: `reason`, `profiles_paused`, `grace_days` |
| `account_billing.charged`   | Monthly per-account billing charged your wallet         | `period`, `accounts`, `amount`, `balance_after`                                                                                    |
| `account_billing.failed`    | Monthly per-account billing could not charge            | `period`, `accounts`, `amount_due`, `error`, `grace_days_remaining`; after grace: `profiles_paused`                                |

### CRM

CRM events fire regardless of whether the change came from the app or the API.

| Event                 | Fires when                      | `data` fields                                                                                              |
| --------------------- | ------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `contact.created`     | A contact is created            | `email`, `contact` `{id, email, name, first_name, last_name, company, phone, tags[], attributes{}}`        |
| `contact.updated`     | A contact is updated            | same as `contact.created`                                                                                  |
| `contact.tag_added`   | A tag is added to a contact     | same as `contact.created`, plus `tag`                                                                      |
| `contact.tag_removed` | A tag is removed from a contact | same as `contact.created`, plus `tag`                                                                      |
| `deal.created`        | An opportunity is created       | `email`, `deal` `{id, name, email, value, stage, status, pipeline_id, assigned_user_id, stage_changed_at}` |
| `deal.stage_changed`  | An opportunity moved stage      | same as `deal.created`, plus `deal.old_stage`                                                              |
| `deal.won`            | An opportunity was marked won   | same as `deal.created`                                                                                     |
| `deal.lost`           | An opportunity was marked lost  | same as `deal.created`                                                                                     |

<Note>
  Machine-readable payload schemas for every event ship in the [OpenAPI spec](https://docs.smartlyq.com/openapi.json) under the standard OpenAPI 3.1 `webhooks` object, so SDK generators and AI agents can consume them.
</Note>
