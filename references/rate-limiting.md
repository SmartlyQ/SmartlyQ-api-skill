<!-- Mirrored from https://docs.smartlyq.com. The docs are the source of truth;
     if this file and the docs disagree, the docs win. -->

# Rate Limiting

> API request limits, posting caps, and how to handle them.

There are two independent limits. **Request limits** govern how often you may call the API. **Posting caps** govern how often a single connected account may publish. A request can pass the first and still be refused by the second.

## Request limits

Your allowance scales with the number of social accounts connected to your workspace, because that is what determines how much work your integration legitimately has to do.

| Connected accounts | Requests per minute | Analytics requests per second |
| ------------------ | ------------------- | ----------------------------- |
| 0 to 2             | 60                  | 6                             |
| 3 to 2,000         | 600                 | 10                            |
| 2,001 and more     | 1,200               | 20                            |

The limit moves as soon as you connect or disconnect an account. There is no separate request limit per platform.

### The analytics burst limit

The analytics endpoints carry an additional per-second ceiling: your per-minute allowance divided by 60, never below 6. It applies to every endpoint requiring the `analytics:read` scope.

This exists so a dashboard refresh cannot spend a whole minute's budget in one burst and then stall. If you hit it, you receive a 429 with `Retry-After: 1`. The rejected request does **not** count against your per-minute allowance.

Every other endpoint is governed by the per-minute window alone.

<Note>
  If your key has a custom rate limit configured, that value is used instead of the table above.
</Note>

## Posting caps

Each connected account has its own daily publishing cap. The caps are per account, so connecting more accounts raises your total throughput; they are not a shared pool.

| Platform             | Posts per day, per account |
| -------------------- | -------------------------- |
| Threads              | 250                        |
| Instagram            | 100                        |
| Facebook             | 100                        |
| X                    | 50                         |
| Pinterest            | 25                         |
| TikTok               | 15 video + 15 photo        |
| Every other platform | 50                         |

TikTok video and photo posts count against separate allowances, so 15 of each per day.

On top of the daily cap, **every account is limited to 25 posts per hour** across all platforms, so a day's allowance cannot be published in a single burst.

When an account is capped, publishing to it is refused before the platform is called, and the response tells you which limit was reached and when to retry. If you publish to several accounts at once, the accounts still under their caps go through; only the capped ones are held back.

## Response headers

Every response includes rate-limit headers:

| Header                  | Description                           |
| ----------------------- | ------------------------------------- |
| `X-RateLimit-Limit`     | Max requests allowed in the window    |
| `X-RateLimit-Remaining` | Requests remaining                    |
| `X-RateLimit-Reset`     | Unix timestamp when the window resets |

## Exceeding a limit

Both request limits return **429 Too Many Requests** with a `Retry-After` header:

```json
{
  "success": false,
  "error": {
    "code": "RATE_LIMIT_EXCEEDED",
    "message": "Rate limit exceeded. Retry after 12 seconds."
  }
}
```

### Two different 429s

A `429` can mean one of two things, and they are handled differently:

| Code                    | Meaning                                                                                                              | What to do                                                                       |
| ----------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `RATE_LIMIT_EXCEEDED`   | You exceeded your own request limit, above.                                                                          | Back off for `Retry-After` seconds.                                              |
| `PLATFORM_RATE_LIMITED` | A connected platform is temporarily limiting publishing for that account. Nothing to do with your request allowance. | Retry that account after the platform's cooldown. Other accounts are unaffected. |

### Handling 429 errors

<Steps>
  <Step title="Read the Retry-After header">
    The header value tells you how many seconds to wait. For an analytics burst it is 1 second.
  </Step>

  <Step title="Back off and retry">
    Use exponential backoff: wait the `Retry-After` value, then double on each subsequent retry.
  </Step>

  <Step title="Spread analytics calls">
    If you are hitting the burst limit, space your analytics calls across the minute rather than firing them together.
  </Step>

  <Step title="Optimize your calls">
    Batch operations where possible and cache responses to reduce call volume.
  </Step>
</Steps>
