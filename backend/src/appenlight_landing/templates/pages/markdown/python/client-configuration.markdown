Title: Python client configuration

# Python client configuration

Install the `appenlight_client` using pip:

    pip install appenlight-client

-----

## Getting started with AppEnlight

To get started, you don't need to set or alter any of the settings mentioned here.
Consult the framework integration pages to start monitoring your app. This page
serves as reference for advanced configurations for large deployments.

## Configuration approaches

Our client supports two ways of configuration: environment variable based and imperative based.

For environment configuration, when starting your application you can set the
variable `APPENLIGHT_KEY` to pass your API key directly, or `APPENLIGHT_INI`
which should hold the absolute path to the configuration file (more on this later).

Alternately, it can use a `settings dictionary` directly which contains various
configuration keys, or a path to ini files which you can generate that allows
full control of client behavior.

The dictionary can hold the exact same keys that the ini file contains, so if
the config file has the `appenlight.foo_bar` key then you are expected to *set the
key with the same name in your settings dict*.


!!! important "Nginx users"
    If you are using `uWSGI` as a deployment method, remember to add the `--enable-threads` option to your uwsgi run command.

## Tips & Tricks

`appenlight_client` supports some non-invasive methods you could use inside of your
application code to customize its behavior on a per-request basis, ie. if you
want to get *log entries or frame local variables from specific views only* or
save some API usage quotas.

You can put the following `keys` into `environ` object:


Key                                             |           Example Value             |           Description
-------------------------------------------     | ----------------------------------  | -------------------------------------
**environ["appenlight.username"]**              | *'username/id'*                     | Allows sending a user identifier so the system can record which errors happened to which users (this is automatic for `django` integration and applications that support the setting `REQUEST_USER` in environ object).
**environ["appenlight.report_local_vars"]**     | *1*                                 | If you don't want to send frame variables globally for all exceptions for performance or bandwidth reasons you can use this directive to override `appenlight.report_local_vars` for single request.
**environ["appenlight.ignore_slow"]**           | *1*                                 | Tells the client not to generate slow reports for this specific view.
**environ["appenlight.ignore_error"]**          | *1*                                 | Tells the client not to generate exception reports for this specific view.
**environ["appenlight.view_name"]**             | *'module/view_name'*                | If you are using a framework that isn't yet officially supported by our client, you can manually set the view name in environ to improve grouping and search quality.
**environ["appenlight.group_string"]**          | *'some/custom/group_str'*           | This value is hashed on the AppEnlight side and used for grouping - completly overriding the project defaults. This is a powerful feature that allows you to set your own custom grouping scheme for AppEnlight.
**environ["appenlight.message"]**               | *"some message"*                    | Provides a convenient way to send a custom message that will be visible in the request details of report.
**environ["appenlight.force_logs"]**            | *1*                                 | Makes the client send logs even if the `appenlight.logging_on_error` directive is in effect; this is very handy when you want to send logs from specific views in your application.
**environ["appenlight.force_send"]**            | *1*                                 | Forces sending client buffers to AppEnlight after this request is finished, useful for debugging a cron job or task worker that may finish its life cycle before 5s(flush time) is met.

## Useful config options

!!! important "Seeing lots of cumulative SQL/slow call usage but not seeing queries/calls info?"
    **Only slow queries are sent to our service** - to conserve API usage on your account
    default client settings to mark queries as slow *are conservative*.

    You may want to alter your `appenlight.ini` config and set default timing options
    to lower values than `0.3s` (default value for marking slow sql queries). See below.


!!! note "Custom client integrations"
    It is extremely important to *instantiate the client as early as possible*, in
    your code, otherwise code execution timing may not work on all supported
    libraries.
    If for some reason you are having problems adding the middleware early enough, do
    not hesitate to instantiate the client manually in your WSGI file.

All of the client capabilities are enabled by default,
but you can change the amount of time a call is considered slow (usually 1s is
considered slow) by passing this variable to client settings ini :

    ::ini
    appenlight.timing.pysolr = 0.1
    appenlight.timing.dbapi2_psycopg2 = 0.1

Or add a key to your settings object :

    ::python
    'appenlight.timing':{'dbapi2_psycopg2':0.1,
                         'dbapi2_MySQLdb':0.1,
                         'timing_pysolr':0.1,
                         }


If for some reason you want to disable timing of specific library - just set the
time value to false.


Additionally, the python client offers a great deal of configuration options.
Here are some of the useful settings you can tweak.

Key                                    |            Description
----------------------------------     | -------------------------------------
**appenlight.server_name**             | identifier for the Instance/Server Name your application is running on : `(default: auto determined fqdn of server)`
**appenlight.transport**               | select one of the possible transport options `(default: appenlight_client.transports.requests:HTTPTransport)`
**appenlight.transport_config**        | config string for the selected transport - you can, for example, change default destination server (for self-hosted AppEnlight) or change the level of error logging for transport `(example: https://self-hosted-appenlight.com?threaded=1&timeout=5&error_log_level=INFO)`
**appenlight.slow_requests**           | record slow requests in an application (needs to be enabled for slow datastore recording) `(default true)`
**appenlight.report_local_vars**       | enables sending frame local vars with exception reports `(default false)`
**appenlight.logging**                 | enable hooking to application loggers `(default true)`
**appenlight.logging.level**           | minimum log level for log capture `(default WARNING)`
**appenlight.logging_on_error**        | send logs only from erroneous/slow requests `(default false)`
**appenlight.slow_request_time**       | time in seconds after a request is considered being slow `(default 3)`
**appenlight.report_404**              | enables 404 error logging `(default False)`
**appenlight.force_send**              | send all data after request is finished *handy for crons or other volatile applications*
**appenlight.environ_keys_whitelist**  | list additional keywords that should be grabbed from an environ object (can be a string with comma separated list of words in lowercase)
**appenlight.request_keys_blacklist**  | list keywords that should be blanked from a request object (can be a string with comma separated list of words in lowercase)
**appenlight.log_namespace_blacklist** | list namespaces that should be ignored when gathering log entries (can be a string with a comma separated list of words in lowercase)

For a full list of config options you can use with example values, please **[consult ini file configuration template](https://github.com/AppEnlight/appenlight-client-python/blob/master/appenlight_client/templates/default_template.ini)**.

## Sensitive data filtering

The client by default blanks out COOKIE, POST, and GET for keys from `appenlight.request_keys_blacklist`
This behaviour can be altered to filter all kinds of data from structures that get sent to the server by passing the dotted module name in the configuration:

    ::ini
    appenlight.filter_callable = foo.bar.baz:callable_name

example:

    ::python
    def callable_name(structure, section=None):
        structure['request']['SOMEVAL'] = '***REMOVED***'
        return structure

AppEnlight will try to import `foo.bar.baz` and use `callable_name` as the
function that accepts parameters `(structure, section)` and returns the altered data structure.
Please note that this functionality can be used to alter things like the App
Enlight grouping mechanism - you can set this variable based on values present
in the structure generated by the client.


## Generating a new ini file

    $ENV/bin/python/appenlight_client makeini appenlight.ini

This will generate a fresh config template for your convenience. **Please edit the file
and update your `API key`**.

## Test communication

    $ENV/bin/python/appenlight_client testini appenlight.ini

**If everything is working as it should, you can proceed to configure your application for use.**
