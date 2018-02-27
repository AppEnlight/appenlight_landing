Title: Reports API Interface

# Reports API Interface

    https://api.appenlight.com/api/reports?protocol_version=0.5

All access to the API is secured by https protocol.

All data is expected to be sent via `json` payloads with the header `Content-Type: application/json`

All requests are normally authenticated by passing headers:

`X-appenlight-api-key: APIKEY` - server side requests

`X-appenlight-public-api-key: PUBLIC_APIKEY` - client side requests(javascript) - you want to use this for `CORS` support

The key values can be passed as query parameters for all endpoints as `public_api_key=YOURPUBKEY`.
This might be required, especially for JavaScript clients.

So all requests like:

    https://api.appenlight.com/api/reports?protocol_version=0.5&public_api_key=XXXX

will work too.

## Anatomy of request to reporting API:

    ::json
    [{
    "client": "your-client-name-python",
    "language": "python",
    "view_name": "views/foo:bar",
    "server": "SERVERNAME/INSTANCENAME",
    "priority": 5,
    "error": "OMG ValueError happened",
    "occurences":1,
    "http_status": 500,
    "tags": [["tag1","value"], ["tag2", 5]],
    "username": "USER",
    "url": "HTTP://SOMEURL",
    "ip": "127.0.0.1",
    "start_time": "2013-12-05T21:46:38.955371",
    "end_time": "2013-12-05T21:47:00.577239",
    "user_agent": "BROWSER_AGENT",
    "extra": [["message","CUSTOM MESSAGE"], ["custom_value", "some payload"]],
    "request_id": "SOME_UUID",
    "request": {"REQUEST_METHOD": "GET",
             "PATH_INFO": "/FOO/BAR",
             "POST": {"FOO":"BAZ","XXX":"YYY"}
             },
    "slow_calls":[{
                   "start": "2011-09-25T21:46:38.974148",
                   "end": "2011-09-25T21:46:39.123188",
                   "type": "sql",
                   "subtype": "postgresql",
                   "parameters": ["QPARAM1","QPARAM2","QPARAMX"],
                   "statement": "QUERY"
                   }],
    "request_stats": {
                    "main": 0.50779,
                    "nosql": 0.01008,
                    "nosql_calls": 17.0,
                    "remote": 0.0,
                    "remote_calls": 0.0,
                    "sql": 0.42423,
                    "sql_calls": 1.0,
                    "tmpl": 0.0,
                    "tmpl_calls": 0.0,
                    "custom": 0.0,
                    "custom_calls": 0.0
                },
    "traceback": [
                {"cline": "return foo_bar_baz(1,2,3)",
                "file": "somedir/somefile.py",
                "fn": "somefunction",
                "module": "somemodule",
                "line": 454,
                "vars": [["a_list",
                         ["1",2,"4","5",6]],
                         ["b", {"1": "2", "ccc": "ddd", "1": "a"}],
                         ["obj", "<object object at 0x7f0030853dc0>"]]
                         },
                {"cline": "OMG ValueError happened",
                "file": "",
                "fn": "",
                "module": "",
                "line": "",
                "vars": []}
                ]
    }]


A request to API is basically a **list** of reports.

A report is a dictionary (array) of values; some of the values
that you can send can be data structures like dictionaries/lists.

**At minimum**, an error report request must contain:

* A **list** with at least one report
* A single report needs to contain at least one **url** or **view_name** keys


Possible keys of a report group object
--------------------------------------

<table class="api-key-info">
<thead>
<th>Parameter</th>
<th>Description</th>
</thead>
<tbody>

<tr>
<td><strong class="key-name">client</strong> <em class="key-req">optional</em>  </td>
<td>
<p>Contains information about what kind of client accessed the API</p>
<p>Example values: "some-custom-client-name"</p>
</td>
</tr>

<tr>
<td><strong class="key-name">language</strong> <em class="key-req">optional</em>  </td>
<td>
<p>Language that the report is generated for - can impact indexing/UI looks</p>
<p>Example values: <code>python</code>, <code>php</code>, <code>javascript</code></p>
</td>
</tr>

<tr>
<td><strong class="key-name">view_name</strong>
<em class="key-req">optional</em>
<em class="key-limits">saved up to 128 chars</em>
</td>
<td>
<p>Specifies the view/code block executed for transaction/web request - used by default in grouping</p>
<p>Example values: <code>views/foo:bar</code></p>
</td>
</tr>

<tr>
<td><strong class="key-name">server</strong>
<em class="key-req">optional</em>
<em class="key-limits">saved up to 128 chars</em>
 </td>
<td>
<p>Specifies the name of the machine or instance that the application is running on - can be used in grouping</p>
<p>Example values: <code>somemachine.network</code></p>
</td>
</tr>

<tr>
<td><strong class="key-name">priority</strong> <em class="key-req">optional</em>  </td>
<td>
<p>Base priority level for the report - <em>default value: 5</em></p>
<p>Example values: <code>3</code></p>
</td>
</tr>

<tr>
<td><strong class="key-name">error</strong>
<em class="key-req">optional</em>
<em class="key-limits">saved up to 512 chars</em>
</td>
<td>
<p>Contains the error/exception text for the report, if not present the reports are being classified as slowness reports
instead exception reports</p>
<p>Example values: <code>TypeError: foo happened</code></p>
</td>
</tr>

<tr>
<td><strong class="key-name">occurences</strong> <em class="key-req">optional</em>  </td>
<td>
<p>Base counter of occurences for the report - <em>default value: 1</em></p>
<p>Example values: <code>128</code></p>
</td>
</tr>

<tr>
<td><strong class="key-name">http_status</strong> <em class="key-req">optional</em>  </td>
<td>
<p>Request HTTP status for the report - <em>default value: 200</em></p>
<p>Example values: <code>500</code></p>
</td>
</tr>

<tr>
<td><strong class="key-name">username</strong> <em class="key-req">optional</em>
 <em class="key-limits">saved up to 255 chars</em>
 </td>
<td>
<p>Contains an identifier of the user that the request failed for</p>
<p>Example values: <code>ergo</code>, <code>5</code> </p>
</td>
</tr>

<tr>
<td><strong class="key-name">url</strong> <em class="key-req">optional</em>
 <em class="key-limits">saved up to 1024 chars</em>
 </td>
<td>
<p>Contains the full request url including get params</p>
<p>Example values: <code>http://127.0.0.1/foo/bar?baz=5</code> </p>
</td>
</tr>

<tr>
<td><strong class="key-name">ip</strong> <em class="key-req">optional</em>
 <em class="key-limits">saved up to 39 chars</em>
 </td>
<td>
<p>Contains the IP address of the client that executed the request</p>
<p>Example values: <code>192.168.0.1</code>, <code>2001:0db8:0000:0000:0000:0000:1428:57ab</code> </p>
</td>
</tr>

<tr>
<td><strong class="key-name">start_time</strong> <em class="key-req">optional</em>  </td>
<td>
<p>Contains the starting time of the request in UTC - will be used to calculate request duration, <em>default: current UTC time of report arrival</em></p>
<p>Example values: <code>2013-12-05T21:46:38.955371</code> </p>
</td>
</tr>

<tr>
<td><strong class="key-name">end_time</strong> <em class="key-req">optional</em>  </td>
<td>
<p>Contains the finish time of the request in UTC - will be used to calculate request duration</p>
<p>Example values: <code>2013-12-05T21:46:39.351371</code> </p>
</td>
</tr>

<tr>
<td><strong class="key-name">user_agent</strong> <em class="key-req">optional</em>
 <em class="key-limits">saved up to 512 chars</em>
 </td>
<td>
<p>Contains the user agent of client that initiated the request</p>
<p>Example values: <code>Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36</code> </p>
</td>
</tr>

<tr>
<td><strong class="key-name">message</strong> <em class="key-req">optional</em>
 <em class="key-limits">saved up to 2048 chars</em>
 </td>
<td>
<p>Contains a custom message attached to report</p>
<p>Example values: <code>I'm attached to this report</code> </p>
</td>
</tr>

<tr>
<td><strong class="key-name">group_string</strong> <em class="key-req">optional</em>
</td>
<td>
<p>All reports sent with the same group string will be grouped together</p>
<p>Example values: <code>86982b00-5fbb-11e4-a252-0002a5d5c51b</code> </p>
</td>
</tr>

<tr>
<td><strong class="key-name">request_id</strong> <em class="key-req">optional</em>
<em class="key-limits">saved up to 40 chars</em>
</td>
<td>
<p>Contains UUID identifier of this report, can be used to corellate log entries with reports - <em>default: generated UUID</em></p>
<p>Example values: <code>86982b00-5fbb-11e4-a252-0002a5d5c51b</code> </p>
</td>
</tr>

<tr>
<td><strong class="key-name">request</strong> <em class="key-req">optional</em>  </td>
<td>
<p>Contains a dictionary object that holds keys and values for HTTP and CGI vars of report's request</em></p>
<p>Example values: <pre>
{"REQUEST_METHOD": "GET",
 "PATH_INFO": "/FOO/BAR",
 "POST": {"FOO":"BAZ","XXX":"YYY"}
}</pre>
</p>

<tr>
<td><strong class="key-name">slow_calls</strong> <em class="key-req">optional</em>  </td>
<td>
<p>Contains a list of dictionaries describing slow calls for this request</em></p>
<p>Example values: <pre>
[
{"start": "2011-09-25T21:46:38.974148",
 "end": "2011-09-25T21:46:39.123188",
 "type": "sql",
 "subtype": "postgresql",
 "parameters": ["QPARAM1","QPARAM2","QPARAMX"],
 "statement": "QUERY"}
]
}
</pre>
</p>
</td>
</tr>


<tr>
<td><strong class="key-name">request_stats</strong> <em class="key-req">optional</em>  </td>
<td>
<p>Contains a dictionary holding current request statistics, where "main" is the total time of the whole request</em></p>
<p>Example values: <pre>
{"main": 0.50779,     # total request time
"nosql": 0.01008,     # time spent executing noSQL datastore calls
"nosql_calls": 17.0,  # number of sql calls
"remote": 0.0,
"remote_calls": 0.0,
"sql": 0.42423,
"sql_calls": 1.0,
"tmpl": 0.0,
"tmpl_calls": 0.0,
"custom": 0.0,
"custom_calls": 0.0}</pre>
</p>
</td>
</tr>

<tr>
<td><strong class="key-name">extra</strong> <em class="key-req">optional</em>  </td>
<td>
<p>Contains a list of key/value pairs that are used to annotate reports with extra information</em></p>
<p>Example values: <pre>[["message","CUSTOM MESSAGE"], ["custom_value", "some payload"]]</pre>
</p>

<tr>
<td><strong class="key-name">tags</strong> <em class="key-req">optional</em>  </td>
<td>
<p>Contains a list of key/value pairs that are used to tag requests for later searching</em></p>
<p>Example values: <pre>[["tag1","value"], ["tag2", 5]]</pre>
</p>


<tr>
<td><strong class="key-name">traceback</strong> <em class="key-req">optional</em>  </td>
<td>
<p>Contains a list of dictionaries describing lines of the exception traceback, having optionally attached framelocal variables to them</em></p>
<p>Example values: <pre>
[
 {"cline": "return foo_bar_baz(1,2,3)",            # current frame line
  "file": "somedir/somefile.py",                   # file location
  "fn": "somefunction",                            # function name
  "module": "module",                              # module name
  "line": 454,                                     # line number
  "vars": [["a_list",                              # variables present in current frame
           ["1",2,"4","5",6]],
          ["b", {"1": "2", "ccc": "ddd", "1": "a"}],
          ["obj", "<object object at 0x7f0030853dc0>"]]},
 {"cline": "OMG ValueError happened",
  "file": "",
  "fn": "",
  "line": "",
  "vars": []}
  ]</pre>
</p>
</td>
</tr>

</tbody>
</table>

