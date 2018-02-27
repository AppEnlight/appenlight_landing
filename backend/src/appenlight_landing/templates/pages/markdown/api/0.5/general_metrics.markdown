Title: General Metrics API Interface

# General Metrics API Interface

    https://api.appenlight.com/api/general_metrics?protocol_version=0.5

All access to the API is secured by https protocol.

All data is expected to be sent via `json` payloads with the header `Content-Type: application/json`

All requests are normally authenticated by passing headers:

`X-appenlight-api-key: APIKEY` - server side requests

`X-appenlight-public-api-key: PUBLIC_APIKEY` - client side requests(javascript) - you want to use this for `CORS` support

The key values can be passed as query parameters for all endpoints as `public_api_key=YOURPUBKEY`.
This might be required, especially for JavaScript clients.

So all requests like:

    https://api.appenlight.com/api/general_metrics?protocol_version=0.5&public_api_key=XXXX

will work too.

## Anatomy of request to metrics API:

    ::json

    [{"timestamp": "2016-01-22T12:12:22Z",
         "namespace": "some.cpu.monitor",
         "server_name": "server.name",
         "tags": [["name", 'cpu.load.01'], ["value", 0.5]]},
    {"timestamp": "2016-01-22T12:12:21Z",
    "namespace": "some.monitor",
    "server_name": "server.name",
    "tags": [["counter_a", 15.5], ["counter_b", 63]]}]

A request to API is a **list** of metrics.

Each entry is a dictionary (array) of values.

**At minimum** a request must contain:

* A list with at least one entry
* Each entry should be a metric dictionary for a separate timestamp/server.
* Each tag needs to be a pair of ["name", float_value] formed in the format outlined above.
