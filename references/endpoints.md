# SmartlyQ API endpoint map

Generated from the published OpenAPI spec at https://docs.smartlyq.com/openapi.json

Base URL: `https://api.smartlyq.com/v1`

296 paths, 385 operations, 33 resource groups.

Use this to find the right endpoint quickly. For request and response
shapes, fetch the spec or the reference page for that operation - do not
guess a body from the summary.

## social (117)

| Method | Path | Operation |
| --- | --- | --- |
| `GET` | `/social/account-groups` | List account groups |
| `POST` | `/social/account-groups` | Create account group |
| `GET` | `/social/account-groups/{group_id}` | Get account group |
| `PUT` | `/social/account-groups/{group_id}` | Update account group |
| `DELETE` | `/social/account-groups/{group_id}` | Delete account group |
| `GET` | `/social/accounts` | List social accounts |
| `GET` | `/social/accounts/follower-stats` | Follower stats |
| `GET` | `/social/accounts/health` | Bulk account health |
| `PATCH` | `/social/accounts/{account_id}` | Rename account |
| `DELETE` | `/social/accounts/{account_id}` | Disconnect a social account |
| `GET` | `/social/accounts/{account_id}/connect-options` | Connection target options |
| `POST` | `/social/accounts/{account_id}/connect-select` | Select connection target |
| `GET` | `/social/accounts/{account_id}/facebook/page` | Get Facebook page details |
| `PATCH` | `/social/accounts/{account_id}/facebook/page` | Update Facebook page details |
| `GET` | `/social/accounts/{account_id}/facebook/page-insights` | Facebook page insights |
| `POST` | `/social/accounts/{account_id}/facebook/page/cover` | Set Facebook page cover photo |
| `POST` | `/social/accounts/{account_id}/facebook/page/picture` | Set Facebook page profile picture |
| `GET` | `/social/accounts/{account_id}/facebook/page/settings` | Get Facebook page settings |
| `PATCH` | `/social/accounts/{account_id}/facebook/page/settings` | Update Facebook page settings |
| `GET` | `/social/accounts/{account_id}/facebook/post-reactions` | Facebook post reactions |
| `GET` | `/social/accounts/{account_id}/facebook/reel-limit` | Get Facebook Reel limit |
| `GET` | `/social/accounts/{account_id}/gmb/attributes` | Get attributes |
| `PUT` | `/social/accounts/{account_id}/gmb/attributes` | Update attributes |
| `GET` | `/social/accounts/{account_id}/gmb/attributes/metadata` | Available attributes |
| `GET` | `/social/accounts/{account_id}/gmb/food-menus` | Get food menus |
| `PUT` | `/social/accounts/{account_id}/gmb/food-menus` | Update food menus |
| `GET` | `/social/accounts/{account_id}/gmb/location` | Get business info |
| `PATCH` | `/social/accounts/{account_id}/gmb/location` | Update business info |
| `GET` | `/social/accounts/{account_id}/gmb/locations` | List Google locations |
| `GET` | `/social/accounts/{account_id}/gmb/media` | List media |
| `POST` | `/social/accounts/{account_id}/gmb/media` | Add photo |
| `DELETE` | `/social/accounts/{account_id}/gmb/media` | Delete media |
| `GET` | `/social/accounts/{account_id}/gmb/performance` | Google Business performance |
| `GET` | `/social/accounts/{account_id}/gmb/place-actions` | List place-action links |
| `POST` | `/social/accounts/{account_id}/gmb/place-actions` | Create place-action link |
| `DELETE` | `/social/accounts/{account_id}/gmb/place-actions` | Delete place-action link |
| `PATCH` | `/social/accounts/{account_id}/gmb/place-actions` | Update place-action link |
| `GET` | `/social/accounts/{account_id}/gmb/search-keywords` | Google Business search keywords |
| `GET` | `/social/accounts/{account_id}/gmb/verifications` | List verifications |
| `POST` | `/social/accounts/{account_id}/gmb/verifications/options` | Verification options |
| `GET` | `/social/accounts/{account_id}/health` | Account health |
| `GET` | `/social/accounts/{account_id}/insights` | Live account insights |
| `GET` | `/social/accounts/{account_id}/instagram/audience` | Instagram audience demographics |
| `GET` | `/social/accounts/{account_id}/instagram/ice-breakers` | Get ice breakers |
| `PUT` | `/social/accounts/{account_id}/instagram/ice-breakers` | Set ice breakers |
| `DELETE` | `/social/accounts/{account_id}/instagram/ice-breakers` | Delete ice breakers |
| `GET` | `/social/accounts/{account_id}/instagram/publishing-limit` | Instagram publishing limit |
| `GET` | `/social/accounts/{account_id}/instagram/stories` | Instagram stories |
| `GET` | `/social/accounts/{account_id}/instagram/stories/{story_id}/insights` | Instagram story insights |
| `GET` | `/social/accounts/{account_id}/mentions` | List mentions |
| `POST` | `/social/accounts/{account_id}/mentions/{mention_id}/reply` | Reply to a mention |
| `GET` | `/social/accounts/{account_id}/messenger/menu` | Get Messenger menu |
| `PUT` | `/social/accounts/{account_id}/messenger/menu` | Set Messenger menu |
| `DELETE` | `/social/accounts/{account_id}/messenger/menu` | Delete Messenger menu |
| `POST` | `/social/accounts/{account_id}/move` | Move account to profile |
| `POST` | `/social/accounts/{account_id}/pause` | Pause posting to an account |
| `GET` | `/social/accounts/{account_id}/pinterest/boards` | Pinterest boards |
| `POST` | `/social/accounts/{account_id}/pinterest/boards` | Create a Pinterest board |
| `GET` | `/social/accounts/{account_id}/reconnect-url` | Account reconnect URL |
| `GET` | `/social/accounts/{account_id}/reddit/feed` | Reddit feed |
| `GET` | `/social/accounts/{account_id}/reddit/search` | Reddit search |
| `GET` | `/social/accounts/{account_id}/reddit/subreddits` | Subscribed subreddits |
| `GET` | `/social/accounts/{account_id}/reddit/subreddits/{subreddit}` | Subreddit info + eligibility |
| `GET` | `/social/accounts/{account_id}/reddit/subreddits/{subreddit}/flairs` | List subreddit post flairs |
| `GET` | `/social/accounts/{account_id}/reddit/subreddits/{subreddit}/rules` | Subreddit rules |
| `POST` | `/social/accounts/{account_id}/resume` | Resume posting to an account |
| `GET` | `/social/accounts/{account_id}/tiktok/creator-info` | TikTok creator info |
| `GET` | `/social/accounts/{account_id}/x/mentions` | X mentions |
| `POST` | `/social/accounts/{account_id}/x/retweets` | Retweet on X |
| `DELETE` | `/social/accounts/{account_id}/x/retweets/{tweet_id}` | Undo retweet |
| `GET` | `/social/accounts/{account_id}/youtube/playlists` | YouTube playlists |
| `PATCH` | `/social/accounts/{account_id}/youtube/playlists/{playlist_id}` | Update a YouTube playlist |
| `GET` | `/social/comments` | List comments |
| `DELETE` | `/social/comments/{comment_id}` | Delete a comment |
| `POST` | `/social/comments/{comment_id}/hide` | Hide or unhide a comment |
| `POST` | `/social/comments/{comment_id}/like` | Like a comment |
| `DELETE` | `/social/comments/{comment_id}/like` | Unlike a comment |
| `POST` | `/social/comments/{comment_id}/moderate` | Approve or reject a comment |
| `POST` | `/social/comments/{comment_id}/private-reply` | Private reply (comment-to-DM) |
| `POST` | `/social/comments/{comment_id}/reply` | Reply to a comment |
| `GET` | `/social/comments/{post_id}` | Get one post's comments (threaded) |
| `POST` | `/social/connect/{platform}` | Start headless account connection |
| `GET` | `/social/connect/{platform}` | Poll headless connection status |
| `GET` | `/social/conversations` | List DM conversations |
| `GET` | `/social/conversations/search` | Search conversations |
| `GET` | `/social/conversations/{conversation_id}` | Get conversation |
| `PATCH` | `/social/conversations/{conversation_id}` | Archive / reopen conversation |
| `GET` | `/social/conversations/{conversation_id}/messages` | List messages in a conversation |
| `POST` | `/social/conversations/{conversation_id}/messages` | Send a direct message |
| `DELETE` | `/social/conversations/{conversation_id}/messages/{message_id}` | Delete a sent message |
| `POST` | `/social/conversations/{conversation_id}/messages/{message_id}/reactions` | React to a message |
| `DELETE` | `/social/conversations/{conversation_id}/messages/{message_id}/reactions` | Remove a message reaction |
| `POST` | `/social/conversations/{conversation_id}/read` | Mark a conversation read |
| `POST` | `/social/conversations/{conversation_id}/typing` | Typing indicator |
| `POST` | `/social/posts` | Create post (publish immediately) |
| `GET` | `/social/posts` | List social posts |
| `POST` | `/social/posts/bulk` | Bulk schedule posts |
| `POST` | `/social/posts/bulk/validate` | Validate a bulk batch |
| `POST` | `/social/posts/schedule` | Schedule post |
| `POST` | `/social/posts/sync-external` | Sync external posts |
| `GET` | `/social/posts/{post_id}` | Get social post |
| `PATCH` | `/social/posts/{post_id}` | Update social post |
| `DELETE` | `/social/posts/{post_id}` | Delete social post |
| `POST` | `/social/posts/{post_id}/edit` | Edit published post |
| `DELETE` | `/social/posts/{post_id}/recycle` | Stop recycling |
| `POST` | `/social/posts/{post_id}/retry` | Retry publishing a post |
| `POST` | `/social/posts/{post_id}/unpublish` | Unpublish post |
| `POST` | `/social/posts/{post_id}/update-metadata` | Update YouTube metadata |
| `GET` | `/social/queues` | List queues |
| `POST` | `/social/queues` | Create queue |
| `GET` | `/social/queues/{queue_id}` | Get queue |
| `PUT` | `/social/queues/{queue_id}` | Update queue |
| `DELETE` | `/social/queues/{queue_id}` | Delete queue |
| `GET` | `/social/queues/{queue_id}/next-slot` | Get next open slot |
| `GET` | `/social/queues/{queue_id}/preview` | Preview upcoming slots |
| `POST` | `/social/validate/media` | Validate media URL |
| `POST` | `/social/validate/post` | Validate post content |

## ads (41)

| Method | Path | Operation |
| --- | --- | --- |
| `GET` | `/ads/accounts` | List connected ad accounts |
| `GET` | `/ads/accounts/diagnostics` | Account health and rate-limit diagnostics |
| `GET` | `/ads/ad-sets` | List ad sets |
| `GET` | `/ads/ad-sets/{id}` | Get an ad set |
| `DELETE` | `/ads/ad-sets/{id}` | Delete an ad set |
| `POST` | `/ads/ad-sets/{id}/archive` | Archive an ad set |
| `POST` | `/ads/ad-sets/{id}/duplicate` | Duplicate an ad set |
| `POST` | `/ads/ad-sets/{id}/pause` | Pause an ad set |
| `POST` | `/ads/ad-sets/{id}/resume` | Resume an ad set |
| `GET` | `/ads/ads` | List ads |
| `GET` | `/ads/ads/{id}` | Get an ad |
| `DELETE` | `/ads/ads/{id}` | Delete an ad |
| `POST` | `/ads/ads/{id}/archive` | Archive an ad |
| `POST` | `/ads/ads/{id}/duplicate` | Duplicate an ad |
| `POST` | `/ads/ads/{id}/pause` | Pause an ad |
| `POST` | `/ads/ads/{id}/resume` | Resume an ad |
| `GET` | `/ads/analytics` | Ads performance analytics |
| `GET` | `/ads/audiences` | List audiences |
| `POST` | `/ads/audiences` | Create an audience |
| `GET` | `/ads/audit-log` | List audit log entries |
| `GET` | `/ads/campaigns` | List campaigns |
| `POST` | `/ads/campaigns` | Create a campaign |
| `POST` | `/ads/campaigns/bulk-status` | Bulk pause/resume campaigns |
| `GET` | `/ads/campaigns/{id}` | Get a campaign |
| `PATCH` | `/ads/campaigns/{id}` | Update a campaign |
| `DELETE` | `/ads/campaigns/{id}` | Delete a campaign |
| `POST` | `/ads/campaigns/{id}/archive` | Archive a campaign |
| `POST` | `/ads/campaigns/{id}/duplicate` | Duplicate a campaign |
| `POST` | `/ads/campaigns/{id}/pause` | Pause a campaign |
| `POST` | `/ads/campaigns/{id}/resume` | Resume a campaign |
| `GET` | `/ads/creatives` | List creatives |
| `POST` | `/ads/creatives` | Create a creative |
| `PATCH` | `/ads/creatives/{id}` | Update a creative |
| `DELETE` | `/ads/creatives/{id}` | Delete a creative |
| `POST` | `/ads/estimate` | Audience-size estimate |
| `GET` | `/ads/lead-forms` | List lead forms |
| `POST` | `/ads/lead-forms` | Create a lead form |
| `GET` | `/ads/pages/{page_id}/posts` | List a Page's organic posts |
| `GET` | `/ads/pixels` | List pixels / conversion destinations |
| `POST` | `/ads/sync` | Trigger an account sync |
| `GET` | `/ads/targeting-search` | Search Meta interest targeting |

## whatsapp (35)

| Method | Path | Operation |
| --- | --- | --- |
| `GET` | `/whatsapp/block-users` | List blocked users |
| `POST` | `/whatsapp/block-users` | Block users |
| `DELETE` | `/whatsapp/block-users` | Unblock users |
| `GET` | `/whatsapp/business-profile` | Get business profile |
| `PATCH` | `/whatsapp/business-profile` | Update business profile |
| `GET` | `/whatsapp/business-profile/display-name` | Get the WhatsApp display name |
| `POST` | `/whatsapp/business-profile/display-name` | Request a WhatsApp display-name change |
| `POST` | `/whatsapp/business-profile/photo` | Set the WhatsApp profile photo |
| `GET` | `/whatsapp/flows` | List flows |
| `POST` | `/whatsapp/flows` | Create a flow |
| `GET` | `/whatsapp/flows/{flow_id}` | Get flow |
| `PATCH` | `/whatsapp/flows/{flow_id}` | Update flow |
| `DELETE` | `/whatsapp/flows/{flow_id}` | Delete flow |
| `POST` | `/whatsapp/flows/{flow_id}/deprecate` | Deprecate flow |
| `PUT` | `/whatsapp/flows/{flow_id}/json` | Upload flow JSON |
| `GET` | `/whatsapp/flows/{flow_id}/json` | Get flow JSON asset |
| `GET` | `/whatsapp/flows/{flow_id}/preview` | Get flow preview URL |
| `POST` | `/whatsapp/flows/{flow_id}/publish` | Publish flow |
| `POST` | `/whatsapp/messages` | Send a WhatsApp message |
| `POST` | `/whatsapp/numbers/{sender_id}/bridge` | Bridge an owned number onto WhatsApp |
| `GET` | `/whatsapp/numbers/{sender_id}/bridge` | Bridge status |
| `POST` | `/whatsapp/numbers/{sender_id}/bridge/request-code` | Request a verification code |
| `POST` | `/whatsapp/numbers/{sender_id}/bridge/verify` | Submit the verification code |
| `GET` | `/whatsapp/phone-numbers` | List phone numbers |
| `GET` | `/whatsapp/sandbox/sessions` | List your sandbox sessions |
| `POST` | `/whatsapp/sandbox/sessions` | Start a sandbox activation |
| `DELETE` | `/whatsapp/sandbox/sessions/{session_id}` | Revoke a sandbox session |
| `POST` | `/whatsapp/sandbox/sessions/{session_id}/send` | Send the sandbox template |
| `GET` | `/whatsapp/template-library` | Browse the shared template library |
| `GET` | `/whatsapp/templates` | List message templates |
| `POST` | `/whatsapp/templates` | Create a message template |
| `POST` | `/whatsapp/templates/from-library` | Adopt a library template |
| `GET` | `/whatsapp/templates/{name}` | Get a WhatsApp template |
| `PATCH` | `/whatsapp/templates/{name}` | Update a WhatsApp template |
| `DELETE` | `/whatsapp/templates/{name}` | Delete a WhatsApp template |

## analytics (19)

| Method | Path | Operation |
| --- | --- | --- |
| `GET` | `/analytics/accounts/{account_id}` | Get account analytics |
| `GET` | `/analytics/best-time` | Best time to post |
| `GET` | `/analytics/content-decay` | Content decay |
| `GET` | `/analytics/daily-metrics` | Daily metrics |
| `GET` | `/analytics/inbox/conversations` | Inbox conversation stats |
| `GET` | `/analytics/inbox/conversations/{conversation_id}` | Conversation analytics |
| `GET` | `/analytics/inbox/heatmap` | Inbox heatmap |
| `GET` | `/analytics/inbox/response-time` | Inbox response time |
| `GET` | `/analytics/inbox/source-breakdown` | Inbox source breakdown |
| `GET` | `/analytics/inbox/top-accounts` | Inbox top accounts |
| `GET` | `/analytics/inbox/volume` | Inbox volume |
| `GET` | `/analytics/overview` | Get analytics overview |
| `GET` | `/analytics/posting-frequency` | Posting frequency vs engagement |
| `GET` | `/analytics/posts` | Get post analytics |
| `GET` | `/analytics/posts/{post_id}/timeline` | Post metric timeline |
| `GET` | `/analytics/youtube/channel-insights` | YouTube channel insights |
| `GET` | `/analytics/youtube/daily-views` | YouTube daily views |
| `GET` | `/analytics/youtube/demographics` | YouTube viewer demographics |
| `GET` | `/analytics/youtube/video-retention` | YouTube audience retention |

## seo (17)

| Method | Path | Operation |
| --- | --- | --- |
| `POST` | `/seo/ai-audit` | AI Visibility Audit (async) |
| `POST` | `/seo/audit` | On-page SEO audit |
| `POST` | `/seo/backlink-anchors` | Backlink anchors |
| `POST` | `/seo/backlink-prospects` | Backlink prospects (link gap) |
| `POST` | `/seo/backlinks-summary` | Backlink profile summary |
| `POST` | `/seo/brand-lookup` | AI Visibility: brand lookup |
| `POST` | `/seo/competitors` | Organic competitors |
| `POST` | `/seo/domain-overview` | Domain rank overview |
| `POST` | `/seo/keyword-difficulty` | Keyword difficulty |
| `POST` | `/seo/keyword-research` | Keyword research |
| `POST` | `/seo/prompt-explorer` | AI Visibility: prompt explorer |
| `POST` | `/seo/rank-history` | Historical rank overview |
| `POST` | `/seo/ranked-keywords` | Ranked keywords (rank tracking) |
| `POST` | `/seo/referring-domains` | Referring domains |
| `POST` | `/seo/serp` | Live SERP lookup |
| `POST` | `/seo/site-audit` | Deep site audit |
| `POST` | `/seo/spam-score` | Backlink spam score |

## contacts (15)

| Method | Path | Operation |
| --- | --- | --- |
| `POST` | `/contacts` | Create or upsert a contact |
| `GET` | `/contacts` | List contacts |
| `POST` | `/contacts/bulk` | Bulk import contacts |
| `GET` | `/contacts/{id}` | Get a contact |
| `PATCH` | `/contacts/{id}` | Update a contact |
| `DELETE` | `/contacts/{id}` | Delete contact |
| `GET` | `/contacts/{id}/channels` | Contact channels |
| `POST` | `/contacts/{id}/enroll` | Enroll a contact in an automation |
| `PUT` | `/contacts/{id}/fields/{slug}` | Set one custom field |
| `DELETE` | `/contacts/{id}/fields/{slug}` | Clear one custom field |
| `POST` | `/contacts/{id}/messages` | Log a message on a contact's timeline |
| `GET` | `/contacts/{id}/notes` | List contact notes |
| `POST` | `/contacts/{id}/notes` | Add a note to a contact |
| `POST` | `/contacts/{id}/tags` | Add tags to a contact |
| `DELETE` | `/contacts/{id}/tags` | Remove tags from a contact |

## automations (11)

| Method | Path | Operation |
| --- | --- | --- |
| `GET` | `/automations` | List automations |
| `GET` | `/automations/{automation_id}` | Get automation |
| `POST` | `/automations/{automation_id}/activate` | Activate automation |
| `POST` | `/automations/{automation_id}/deactivate` | Pause automation |
| `POST` | `/automations/{automation_id}/duplicate` | Duplicate an automation |
| `GET` | `/automations/{automation_id}/runs` | List runs |
| `GET` | `/automations/{automation_id}/runs/{run_id}` | Get run |
| `POST` | `/automations/{automation_id}/trigger` | Trigger automation |
| `GET` | `/automations/{automation_id}/versions` | List automation versions |
| `GET` | `/automations/{automation_id}/versions/{version}` | Get one automation version |
| `POST` | `/automations/{automation_id}/versions/{version}/restore` | Restore an automation version |

## chatbots (10)

| Method | Path | Operation |
| --- | --- | --- |
| `POST` | `/chatbots` | Create chatbot |
| `GET` | `/chatbots` | List chatbots |
| `GET` | `/chatbots/{id}` | Get chatbot |
| `PATCH` | `/chatbots/{id}` | Update chatbot |
| `DELETE` | `/chatbots/{id}` | Delete chatbot |
| `GET` | `/chatbots/{id}/conversations` | List chatbot conversations |
| `GET` | `/chatbots/{id}/conversations/{conv_id}/messages` | Get conversation messages |
| `POST` | `/chatbots/{id}/messages` | Send chatbot message |
| `POST` | `/chatbots/{id}/train` | Start chatbot training |
| `GET` | `/chatbots/{id}/train-status` | Get chatbot training status |

## profiles (10)

| Method | Path | Operation |
| --- | --- | --- |
| `POST` | `/profiles` | Create a profile |
| `GET` | `/profiles` | List profiles |
| `GET` | `/profiles/{id}` | Get a profile |
| `DELETE` | `/profiles/{id}` | Delete a profile |
| `PATCH` | `/profiles/{id}` | Update a profile |
| `GET` | `/profiles/{id}/accounts` | List a profile's connected accounts |
| `POST` | `/profiles/{id}/connect-link` | Create a hosted connect link |
| `POST` | `/profiles/{id}/connect/{platform}` | Get a raw connect URL for one platform |
| `POST` | `/profiles/{id}/pause` | Pause a profile |
| `POST` | `/profiles/{id}/resume` | Resume a profile |

## workspaces (10)

| Method | Path | Operation |
| --- | --- | --- |
| `POST` | `/workspaces` | Create a workspace (sub-account) |
| `GET` | `/workspaces` | List workspaces (sub-accounts) |
| `POST` | `/workspaces/bulk` | Bulk sub-account action |
| `GET` | `/workspaces/{id}` | Get a workspace (sub-account) |
| `DELETE` | `/workspaces/{id}` | Delete a workspace (sub-account) |
| `POST` | `/workspaces/{id}/disable-saas` | Disable SaaS mode for a workspace |
| `POST` | `/workspaces/{id}/pause` | Pause (suspend) a workspace |
| `POST` | `/workspaces/{id}/resume` | Resume a paused workspace |
| `GET` | `/workspaces/{id}/subscription` | Get a sub-account's subscription |
| `GET` | `/workspaces/{id}/wallet` | Get a sub-account's wallet balance |

## videos (9)

| Method | Path | Operation |
| --- | --- | --- |
| `GET` | `/videos` | List videos |
| `POST` | `/videos/broll-suggest` | Suggest B-roll moments |
| `POST` | `/videos/emphasis` | Suggest on-screen emphasis |
| `POST` | `/videos/generate` | Generate video |
| `POST` | `/videos/hook` | Generate a viral hook line |
| `GET` | `/videos/models` | List available video models |
| `POST` | `/videos/viral-thumbnail` | Generate a viral thumbnail |
| `GET` | `/videos/{video_id}` | Get video |
| `DELETE` | `/videos/{video_id}` | Delete video |

## companies (7)

| Method | Path | Operation |
| --- | --- | --- |
| `GET` | `/companies` | List companies |
| `POST` | `/companies` | Create a company |
| `GET` | `/companies/{id}` | Get a company |
| `PATCH` | `/companies/{id}` | Update a company |
| `DELETE` | `/companies/{id}` | Delete a company |
| `POST` | `/companies/{id}/contacts` | Link a contact to a company |
| `DELETE` | `/companies/{id}/contacts` | Unlink a contact from a company |

## webhooks (7)

| Method | Path | Operation |
| --- | --- | --- |
| `GET` | `/webhooks` | List webhooks |
| `POST` | `/webhooks` | Create webhook |
| `POST` | `/webhooks/deliveries/{id}/replay` | Replay a webhook delivery |
| `GET` | `/webhooks/logs` | List webhook delivery logs |
| `DELETE` | `/webhooks/{id}` | Delete webhook |
| `PUT` | `/webhooks/{id}` | Update webhook |
| `POST` | `/webhooks/{id}/test` | Send test webhook |

## media (6)

| Method | Path | Operation |
| --- | --- | --- |
| `GET` | `/media` | List media |
| `POST` | `/media/upload-direct` | Upload a file directly |
| `POST` | `/media/upload-url` | Get presigned upload URL |
| `GET` | `/media/{media_id}` | Get media |
| `DELETE` | `/media/{media_id}` | Delete media |
| `POST` | `/media/{media_id}/confirm` | Confirm a presigned upload |

## opportunities (6)

| Method | Path | Operation |
| --- | --- | --- |
| `GET` | `/opportunities` | List opportunities |
| `POST` | `/opportunities` | Create an opportunity |
| `GET` | `/opportunities/{id}` | Get an opportunity |
| `PATCH` | `/opportunities/{id}` | Update an opportunity |
| `DELETE` | `/opportunities/{id}` | Delete an opportunity |
| `POST` | `/opportunities/{id}/status` | Update opportunity status |

## tasks (6)

| Method | Path | Operation |
| --- | --- | --- |
| `GET` | `/tasks` | List tasks |
| `POST` | `/tasks` | Create a task |
| `GET` | `/tasks/{id}` | Get a task |
| `PATCH` | `/tasks/{id}` | Update a task |
| `DELETE` | `/tasks/{id}` | Delete a task |
| `POST` | `/tasks/{id}/time` | Log time on a task |

## urls (6)

| Method | Path | Operation |
| --- | --- | --- |
| `GET` | `/urls` | List short URLs |
| `POST` | `/urls/shorten` | Shorten URL |
| `PATCH` | `/urls/{id}` | Update a short URL |
| `GET` | `/urls/{url_id}` | Get short URL |
| `DELETE` | `/urls/{url_id}` | Delete short URL |
| `GET` | `/urls/{url_id}/stats` | Get short URL stats |

## me (5)

| Method | Path | Operation |
| --- | --- | --- |
| `GET` | `/me` | Get current user profile |
| `GET` | `/me/account-billing` | Account billing summary |
| `GET` | `/me/balance` | Get wallet balance |
| `GET` | `/me/billing` | Billing overview |
| `GET` | `/me/usage` | Get usage summary |

## tags (5)

| Method | Path | Operation |
| --- | --- | --- |
| `GET` | `/tags` | List tags |
| `POST` | `/tags` | Create a tag |
| `POST` | `/tags/delete` | Delete a tag |
| `POST` | `/tags/merge` | Merge tags |
| `POST` | `/tags/rename` | Rename a tag |

## articles (4)

| Method | Path | Operation |
| --- | --- | --- |
| `GET` | `/articles` | List articles |
| `POST` | `/articles/generate` | Generate article |
| `GET` | `/articles/{article_id}` | Get article |
| `DELETE` | `/articles/{article_id}` | Delete article |

## calendar (4)

| Method | Path | Operation |
| --- | --- | --- |
| `POST` | `/calendar/bookings` | Take a booking |
| `POST` | `/calendar/bookings/{id}/cancel` | Cancel a booking |
| `GET` | `/calendar/event-types` | List booking pages |
| `GET` | `/calendar/slots` | List open slots |

## custom-fields (4)

| Method | Path | Operation |
| --- | --- | --- |
| `GET` | `/custom-fields` | List custom fields |
| `POST` | `/custom-fields` | Create a custom field |
| `DELETE` | `/custom-fields/{id}` | Delete a custom field |
| `PATCH` | `/custom-fields/{id}` | Update custom field |

## images (4)

| Method | Path | Operation |
| --- | --- | --- |
| `GET` | `/images` | List images |
| `POST` | `/images/generate` | Generate image |
| `GET` | `/images/{image_id}` | Get image |
| `DELETE` | `/images/{image_id}` | Delete image |

## presentations (4)

| Method | Path | Operation |
| --- | --- | --- |
| `GET` | `/presentations` | List presentations |
| `POST` | `/presentations/generate` | Generate presentation |
| `GET` | `/presentations/{presentation_id}` | Get presentation |
| `DELETE` | `/presentations/{presentation_id}` | Delete presentation |

## reviews (4)

| Method | Path | Operation |
| --- | --- | --- |
| `GET` | `/reviews` | List reviews |
| `POST` | `/reviews/sync` | Sync reviews |
| `POST` | `/reviews/{review_id}/reply` | Reply to review |
| `DELETE` | `/reviews/{review_id}/reply` | Delete review reply |

## audio (3)

| Method | Path | Operation |
| --- | --- | --- |
| `POST` | `/audio/speech-to-text` | Speech to text |
| `POST` | `/audio/text-to-speech` | Text to speech |
| `GET` | `/audio/{audio_id}` | Get audio |

## captain (3)

| Method | Path | Operation |
| --- | --- | --- |
| `GET` | `/captain/conversations` | List AI Captain conversations |
| `GET` | `/captain/conversations/{conversation_id}` | Get AI Captain conversation |
| `POST` | `/captain/messages` | Send AI Captain message |

## jobs (3)

| Method | Path | Operation |
| --- | --- | --- |
| `GET` | `/jobs` | List jobs |
| `GET` | `/jobs/{job_id}` | Get job |
| `POST` | `/jobs/{job_id}/cancel` | Cancel job |

## shorts (3)

| Method | Path | Operation |
| --- | --- | --- |
| `GET` | `/shorts` | List shorts jobs |
| `POST` | `/shorts/generate` | Generate viral shorts from a long video |
| `GET` | `/shorts/{uid}` | Get shorts job + clips |

## content (2)

| Method | Path | Operation |
| --- | --- | --- |
| `POST` | `/content/caption` | Generate a social caption |
| `POST` | `/content/rewrite` | Rewrite content |

## pipelines (2)

| Method | Path | Operation |
| --- | --- | --- |
| `GET` | `/pipelines` | List pipelines |
| `POST` | `/pipelines` | Create a pipeline |

## saas (2)

| Method | Path | Operation |
| --- | --- | --- |
| `GET` | `/saas/plans` | List SaaS plans |
| `GET` | `/saas/plans/{id}` | Get a SaaS plan |

## logs (1)

| Method | Path | Operation |
| --- | --- | --- |
| `GET` | `/logs` | List developer logs |
