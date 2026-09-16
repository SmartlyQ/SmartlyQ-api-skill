<!-- Mirrored from https://docs.smartlyq.com. The docs are the source of truth;
     if this file and the docs disagree, the docs win. -->

# Rate Limiting

> API rate limits and how to handle them.

## Default limits

Every API key is rate-limited to prevent abuse and ensure fair access.

| Limit               | Default              |
| ------------------- | -------------------- |
| Requests per minute | 60                   |
| Per-key override    | Configurable per key |

## Response headers

Every response includes rate-limit headers:

| Header                  | Description                           |
| ----------------------- | ------------------------------------- |
| `X-RateLimit-Limit`     | Max requests allowed in the window    |
| `X-RateLimit-Remaining` | Requests remaining                    |
| `X-RateLimit-Reset`     | Unix timestamp when the window resets |

## Exceeding the limit

When you exceed the limit, the API returns **429 Too Many Requests** with a `Retry-After` header:

```json
{
  "success": false,
  "error": {
    "code": "RATE_LIMITED",
    "message": "Too many requests. Retry after 12 seconds."
  }
}
```

### Handling 429 errors

<Steps>
  <Step title="Read the Retry-After header">
    The header value tells you how many seconds to wait.
  </Step>

  <Step title="Back off and retry">
    Use exponential backoff: wait the `Retry-After` value, then double on each subsequent retry.
  </Step>

  <Step title="Optimize your calls">
    Batch operations where possible and cache responses to reduce call volume.
  </Step>
</Steps>
