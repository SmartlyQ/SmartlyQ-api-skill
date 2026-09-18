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

| Code  | Meaning                                                                                                                               |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------- |
| `200` | Success                                                                                                                               |
| `201` | Created                                                                                                                               |
| `202` | Accepted (async job queued)                                                                                                           |
| `204` | No Content (resource deleted)                                                                                                         |
| `400` | Bad Request — invalid parameters                                                                                                      |
| `401` | Unauthorized — missing or invalid API key                                                                                             |
| `402` | Payment Required — insufficient credits                                                                                               |
| `403` | Forbidden — valid key but insufficient scope                                                                                          |
| `404` | Not Found — resource does not exist                                                                                                   |
| `409` | Conflict — duplicate request (idempotency)                                                                                            |
| `422` | Unprocessable Entity - validation error, or a connected platform or provider refused the request (`error.message` carries its reason) |
| `429` | Too Many Requests — rate limited                                                                                                      |
| `500` | Internal Server Error                                                                                                                 |
| `502` | Bad Gateway - a connected platform could not be reached at all. Sent without a JSON body. Retry after a short delay.                  |

## Common error codes

| Code                           | Description                                                                                                                                                                                                                                                                                                                                |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `UNAUTHORIZED`                 | API key is missing or invalid                                                                                                                                                                                                                                                                                                              |
| `FORBIDDEN`                    | Key lacks the required scope                                                                                                                                                                                                                                                                                                               |
| `CONNECTION_SCOPE_MISSING`     | The connected social account is missing a permission this call needs, usually because it was connected before SmartlyQ requested that permission. Reconnect the account to fix it; `details.reconnect_required` is `true`.                                                                                                                 |
| `INSUFFICIENT_CREDITS`         | Wallet balance too low                                                                                                                                                                                                                                                                                                                     |
| `RATE_LIMIT_EXCEEDED`          | You exceeded your own request limit. See [rate limiting](/guides/rate-limiting).                                                                                                                                                                                                                                                           |
| `PLATFORM_RATE_LIMITED`        | A connected platform is temporarily limiting publishing for that account. Retryable: back off and retry after the cooldown.                                                                                                                                                                                                                |
| `LIMIT_REACHED`                | You have reached a limit on your account, such as the 200 sub-account cap. Delete what you no longer need, or email [support@smartlyq.com](mailto:support@smartlyq.com) to have it raised.                                                                                                                                                 |
| `CONTENT_POLICY_VIOLATION`     | The post breaches the [Content Policy](https://smartlyq.com/legal/content-policy) and was not created. Not retryable: edit the content, or contact support if you believe the decision is wrong.                                                                                                                                           |
| `VALIDATION_ERROR`             | Request body failed validation                                                                                                                                                                                                                                                                                                             |
| `RESOURCE_NOT_FOUND`           | The requested resource does not exist                                                                                                                                                                                                                                                                                                      |
| `IDEMPOTENCY_CONFLICT`         | A request with this idempotency key was already processed                                                                                                                                                                                                                                                                                  |
| `MODEL_NOT_AVAILABLE`          | The requested AI model is not available on your plan                                                                                                                                                                                                                                                                                       |
| `JOB_FAILED`                   | An async job encountered an error                                                                                                                                                                                                                                                                                                          |
| `POST_TYPE_UNSUPPORTED`        | `platform_options.<platform>.type` names a post format this platform cannot publish. The message lists the accepted values; see [Platform options](/guides/platform-options).                                                                                                                                                              |
| `PLATFORM_DAILY_LIMIT_REACHED` | HTTP `422`, not retryable. The platform's daily limit for this post type is used up for a selected account - today, Facebook's 30 Reels per Page in a moving 24-hour window. Nothing is created. Publish after `details.next_available_at`, or send the post as a different type. `details` also carries `account_id`, `limit` and `used`. |
| `PLATFORM_ERROR`               | HTTP `422`. The connected platform refused the request, for example an expired token or a value it does not accept. `error.message` includes the platform's own reason. Fix the request or reconnect the account; retrying the same request will fail the same way.                                                                        |
| `PLATFORM_UPSTREAM_ERROR`      | HTTP `422` from the WhatsApp endpoints: WhatsApp refused the request, with its reason in `error.message`. HTTP `502` only when WhatsApp could not be reached.                                                                                                                                                                              |
| `PROVIDER_ERROR`               | HTTP `422`. An AI or media provider could not produce a result. When `retryable` is `true`, the same request can succeed on a second try.                                                                                                                                                                                                  |

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
