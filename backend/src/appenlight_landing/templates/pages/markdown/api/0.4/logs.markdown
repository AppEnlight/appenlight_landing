Title: Logging API Interface

# Logging API Interface

    https://api.appenlight.com/api/logs?protocol_version=0.4

All access to the API is secured by https protocol.

All data is expected to be sent via `json` payloads with header `Content-Type: application/json`

All requests are normally authenticated by passing headers:

`X-appenlight-api-key: APIKEY` - server side requests

`X-appenlight-public-api-key: PUBLIC_APIKEY` - client side requests(javascript) - you want to use this for `CORS` support

The key values can be passed as query parameters for all endpoints as `public_api_key=YOURPUBKEY`,
this might be required especially for Javascript clients.

So all requests like:

    https://api.appenlight.com/api/logs?protocol_version=0.4&public_api_key=XXXX

Will work too.

## Anatomy of request to log API:

    ::json
    [
      {
      "log_level": "WARN",
      "message": "OMG ValueError happened",
      "namespace": "some.namespace.indicator",
      "request_id": "SOME_UUID",
      "server": "some.server.hostname",
      "date": "2011-09-25T21:46:38.955371",
      "tags": [["tag1","value"], ["tag2", 5]]
      },
      {
      "log_level": "ERROR",
      "message": "OMG ValueError happened2",
      "namespace": "some.namespace.indicator",
      "request_id": "SOME_UUID",
      "server": "some.server.hostname",
      "date": "2011-09-25T21:46:38.955371"
      }
    ]

Request to api is a **list** of log messages.

Each entry is a dictionary(array) of values.

**At minimum** request must contain:

* A list with at least one entry
* Entry should contain following keys: **message**
* Whole HTTP body of API request needs to be less than **1024kb**


Possible keys of log object
---------------------------

<table class="api-key-info">
<thead>
<th>Parameter</th>
<th>Description</th>
</thead>
<tbody>

<tr>
<td><strong class="key-name">log_level</strong> <em class="key-req">optional</em>
  <em class="key-limits">saved up to 10 chars</em>
 </td>
<td>
<p>Contains severity level for log entry</p>
<p>Example values: <code>info</code>, <code>error</code>, <code>critical</code> </p>
</td>
</tr>

<tr>
<td><strong class="key-name">message</strong> <em class="key-req">optional</em>
 <em class="key-limits">saved up to 4096 chars</em>
 </td>
<td>
<p>Contains actual log message body</p>
<p>Example values: <code>Something happened here</code> </p>
</td>
</tr>

<tr>
<td><strong class="key-name">namespace</strong> <em class="key-req">optional</em>
 <em class="key-limits">saved up to 128 chars</em>
 </td>
<td>
<p>Identifies the origin of log message</p>
<p>Example values: <code>package.module</code>, <code>apache:logs</code> </p>
</td>
</tr>

<tr>
<td><strong class="key-name">request_id</strong> <em class="key-req">optional</em>
 <em class="key-limits">saved up to 40 chars</em>
 </td>
<td>
<p>Contains UUID identifier of request that generated the report, can be used to corellate log entries with reports/same transaction</p>
<p>Example values: <code>86982b00-5fbb-11e4-a252-0002a5d5c51b</code> </p>
</td>
</tr>

<tr>
<td><strong class="key-name">server</strong> <em class="key-req">optional</em>
 <em class="key-limits">saved up to 128 chars</em>
 </td>
<td>
<p>Specifies the name of machine or instance that the application is running on</p>
<p>Example values: <code>somemachine.network</code></p>
</td>
</tr>

<tr>
<td><strong class="key-name">date</strong> <em class="key-req">optional</em>  </td>
<td>
<p>Contains the log creation time of in UTC - will be used to calculate request duration, <em>default: current UTC time of report arrival</em></p>
<p>Example values: <code>2013-12-05T21:46:38.955371</code> </p>
</td>
</tr>

<tbody>
</table>