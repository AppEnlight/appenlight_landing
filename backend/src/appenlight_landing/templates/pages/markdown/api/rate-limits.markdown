Title: Rate Limits

# Rate Limits

AppEnlight collects a lot of data every minute. Due to this, there are limits
to how much your app can send via API.

Your application can send up to `20 reports per 10 seconds`; after this limit is
reached, AppEnlight will respond with a `429 TooManyRequests` code for subsequent
client requests. The counter resets after `10 seconds`.

Also, after your error reaches `200 occurences` (grouped errors), AppEnlight will
automatically start rate-limiting your errors, storing only Nth `request_detail`
that you send using a rate limiting algorithm: every 2nd request detail after
200 occurences, every 3rd after 300, and so on...
