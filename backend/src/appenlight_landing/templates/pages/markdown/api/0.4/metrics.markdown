Title: Metrics API Interface

# Metrics API Interface

    https://api.appenlight.com/api/request_stats?protocol_version=0.4

All access to the API is secured by https protocol.

All data is expected to be sent via `json` payloads with header `Content-Type: application/json`

All requests are normally authenticated by passing headers:

`X-appenlight-api-key: APIKEY` - server side requests

`X-appenlight-public-api-key: PUBLIC_APIKEY` - client side requests(javascript) - you want to use this for `CORS` support

The key values can be passed as query parameters for all endpoints as `public_api_key=YOURPUBKEY`,
this might be required especially for Javascript clients.

So all requests like:

    https://api.appenlight.com/api/request_stats?protocol_version=0.4&public_api_key=XXXX

Will work too.

## Anatomy of request to log API:

    ::json

    [{"server": "some.server.hostname",
      "timestamp": "2014-07-20T21:38:00",
      "metrics": [["dir/module:func",
                   {"custom": 0.0,
                    "custom_calls": 0,
                    "main": 0.01664,
                    "nosql": 0.00061,
                    "nosql_calls": 23,
                    "remote": 0.0,
                    "remote_calls": 0,
                    "requests": 1,
                    "sql": 0.00105,
                    "sql_calls": 2,
                    "tmpl": 0.0,
                    "tmpl_calls": 0}],
                  ["SomeView.function",
                   {"custom": 0.0,
                    "custom_calls": 0,
                    "main": 0.647261,
                    "nosql": 0.306554,
                    "nosql_calls": 140,
                    "remote": 0.0,
                    "remote_calls": 0,
                    "requests": 28,
                    "sql": 0.0,
                    "sql_calls": 0,
                    "tmpl": 0.0,
                    "tmpl_calls": 0}]]
                    }]

Request to api is a **list** of metrics.

Each entry is a dictionary(array) of values.

**At minimum** request must contain:

* A list with at least one entry
* Each entry should be a metrics dictionary for separate time interval (grouped per minute) holding request stats for each view/controller of application.
* Each request stat needs to be a pair of ["view_name", {view_stats}] formed in format outlined above, `*_calls` keys contain number of calls that were executed during requests for corresponding layer,
keys that do not contain `*_calls` will hold the time in seconds that application spent executing code/waiting for data in a given application layer.