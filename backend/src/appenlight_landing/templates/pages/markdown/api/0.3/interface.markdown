Title: API Interface

# API Interface

All access to the API is secured by https protocol.

All data is expected to be sent via `json` payloads with header `Content-Type: application/json`

All requests are normally authenticated by passing headers:

`X-errormator-api-key: APIKEY` - server side requests

`X-errormator-public-api-key: PUBLIC_APIKEY` - client side requests(javascript) - you want to use this for `CORS` support

The key values can be passed as query parameters for all endpoints as `public_api_key=YOURPUBKEY` and `api_key=YOURKEY`,
this might be required especially for Javascript clients.

So all requests like:

    https://api.appenlight.com/api/ENDPOINT?protocol_version=0.3&api_key=XXXX
    https://api.appenlight.com/api/ENDPOINT?protocol_version=0.3&public_api_key=XXXX

Will work too.

## Error reports API endpoint

    `https://api.appenlight.com/api/reports?protocol_version=0.3`

Anatomy of request to reporting API:

    ::json
    [
      {"client": "python",
      "traceback": "TRACEBACK TEXT",
      "server": "SERVERNAME/INSTANCENAME",
      "priority": 5,
      "error": "OMG ValueError happened",
      "occurences":1,
      "http_status": 500,
      "report_details": [
                         {"username": "USER",
                         "url": "HTTP://SOMEURL",
                         "ip": "127.0.0.1",
                         "start_time": "2011-09-25T21:46:38.955371",
                         "user_agent": "BROWSER_AGENT",
                         "message": "CUSTOM MESSAGE",
                         "request_id": "SOME_UUID",
                         "request": {"REQUEST_METHOD": "GET",
                                     "PATH_INFO": "/FOO/BAR",
                                     "POST": {"FOO":"BAZ","XXX":"YYY"}
                                     }
                         }]
    }]


Request to api is basicly a **list** of errors.

An error is a dictionary(array) of values, some of values 
that you can send be data structures like dictionaries/lists.

Possible data you can currenty send:

* **http_status** HTTP status of the request **default** *200* 
* **priority** Priority of the error **default** *1* 
* **error** Error/Exception name, saved up to 500 characters
* **server** server/instance name, saved up to 255 characters
* **traceback** (stacktrace), saved up to 10000 characters
* **report_details** Contains entries describing separate requests that made the error appear, its a list of **dictionary objects**
* **occurences**  How many times error occured **default** *1* 
* **client** Used to determine what kind of client sent information, useful for future postprocessing information
* **group_string** Used to determine how to group errors together - default: url+error hash

**At minimum** error report request must contain:

* A list with at least one report
* Error needs to contain following keys: **error, report_details**
* report_details field needs to be a **list** containing at least one separate report(request) detail
* a single request_detail dictionary needs to contain at least following key: **url**, **request_id** 
* Whole HTTP body of API request needs to be less than **75kb**


-----------

## Logging API endpoint

    `https://api.appenlight.com/api/logs?protocol_version=0.3`

Anatomy of request to log API:

    ::json
    [
      {
      "log_level": "WARN",
      "message": "OMG ValueError happened",
      "namespace": "some.namespace.indicator",
      "request_id": "SOME_UUID",
      "server": "some server",
      "date": "2011-09-25T21:46:38.955371"
      },
      {
      "log_level": "ERROR",
      "message": "OMG ValueError happened2",
      "namespace": "some.namespace.indicator",
      "request_id": "SOME_UUID",
      "server": "some server",
      "date": "2011-09-25T21:46:38.955371"
      }
    ]

Request to api is a **list** of log messages.

Each entry is a dictionary(array) of values

**At minimum** request must contain:

* A list with at least one entry
* Entry needs to contain following keys: **log_level, message**
* **log_level** field needs not to exceed **10 characters**, otherwise will be truncated
* Whole HTTP body of API request needs to be less than **75kb**

-----------

## Slow request/query API endpoint

    `https://api.appenlight.com/api/slow_reports?protocol_version=0.3`

Anatomy of request to slow request reporting API:

    ::json
    [
        {
        "client": "client_language",
        "server": "SERVER_NAME",
        "report_details": [
                            {
                            "start_time": "2011-09-25T21:46:38.955371",
                            "end_time": "2011-09-25T21:47:00.577239",
                            "username": "USER",
                            "url": "HTTP://SOMEURL",
                            "ip": "127.0.0.1",
                            "user_agent": "BROWSER_AGENT",
                            "message": "CUSTOM MESSAGE",
                            "request_id": "SOME_UUID",
                            "request": {"POST": {"FOO":"BAZ","XXX":"YYY"}},
                            "slow_calls":[
                                          {"duration": 11.2424,
                                           "timestamp": "2011-09-25T21:46:38.974148",
                                           "type": "sql",
                                           "subtype": "postgresql",
                                           "parameters": ["QPARAM1","QPARAM2","QPARAMX"],
                                           "statement": "QUERY"}]
                            }]
        }                        
    ]

Request to api is a **list** of slow request reports.

An error is a dictionary(array) of values, some of values  
that you can send be data structures like dictionaries/lists.

Possible data you can currenty send:

* **url** URL of the request
* **start_time** Start time of request
* **end_time** Time request finished
* **server** server/instance name, saved up to 255 characters
* **request** Should contain information useful to identify cause of slowness 
  **default** *1* 
* **report_details** Contains entries describing separate slow queries/calls to 
  datastore, its a list of **dictionary objects**
* **client** Used to determine what kind of client sent information, useful for future postprocessing information


**At minimum** slow report request must contain:

* A list with at least one report
* report_details field needs to be a **list** containing at least one separate report(request) detail
* a single request_detail dictionary needs to contain at least following key: **url**, **request_id** 
* Whole HTTP body of API request needs to be less than **75kb**
