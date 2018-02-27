Title: Javascript error monitoring

# Javascript error monitoring

-----

## Include the script on your page

First, please obtain the latest copy of the javascript client from our
[**Github repository**](https://github.com/AppEnlight/appenlight-client-js).

Or use the CDN hosted version from jsDelivr (http://www.jsdelivr.com/#!appenlight).

Next, you can include the file on your pages directly or asynchroneously:

    ::javascript
    var initAppEnlight = function () {
      if(this.readyState!='loading'){
          AppEnlight.init({
              apiKey:'PUBLIC_API_KEY',
              windowOnError: 1 // enable to hook to window.onerror
          });
          // setting request info is completly optional
          AppEnlight.setRequestInfo({
              server:'servername',
              username:'i_am_mario',
              ip: "127.0.0.1",
              request_id:"server_generated_uuid"
          });
      }
    };
    //  load the script asynchroneously
    var scrElem = document.createElement('script');
    scrElem.type = 'text/javascript';
    scrElem.async = true;
    scrElem.onload = scrElem.onreadystatechange = initAppEnlight;
    scrElem.src = "//cdn.jsdelivr.net/appenlight/0.5/appenlight-client.min.js";
    var p = document.getElementsByTagName('script')[0];
    p.parentNode.insertBefore(scrElem, p);

At this point, the client is configured and will automaticly stream all data to
our servers once every second if it has anything in its buffers.

!!! note "Client auto update"
    You can point the CDN version to `//cdn.jsdelivr.net/appenlight/latest/appenlight-client.min.js`
    if you want to always point to the newest release available.
    We try to avoid backwards incompatible changes, but in case a change like that
    is introduced it might cause issues with your application.

If the `windowOnError` config option is enabled, the client will process all unhandled
exceptions for you. Remember though that window.onerror stacks contain a minimal amount
of information; for best results, you will want to do explict exception catching.

Please *avoid* throwing string exceptions, if possible use `throw new Error()` instead.

** EXPLICIT ERROR CATCHING - EXAMPLE**::

    ::javascript
    try{
      1 + non_existing_var;
    }catch(exc){
      AppEnlight.grabError(exc);
    }


**LOGGING**

The log level (one of ``debug``, ``info``, ``warning``, ``error``, or
``critical``) and a message are required for each log call::

    AppEnlight.log('error','some test message');
    AppEnlight.log('info','some info message');
    AppEnlight.log('warning','some warn message');


The ``log`` method supports three additional arguments for customization of
the namespace, a unique ID for grouping logs, and tags. To avoid overriding
global values, use ``undefined`` for the namespace value::

    AppEnlight.log('info', 'Message A');                       // Default namespace, window.location.pathname
    AppEnlight.setGlobalNamespace('my_script');
    AppEnlight.log('info', 'Message B');                       // Global namespace, my_script
    AppEnlight.log('info', 'Message C', 'script_main');        // Custom namespace script_main
    AppEnlight.log('info', 'Message C', null, requestID);      // null namespace
    AppEnlight.log('info', 'Message C', undefined, requestID); // Global namespace, my_script


**GLOBAL CONFIGURATION**

**Namespace**

The namespace can be provided on each ``log`` call or applied to all logging
via the global ``namespace`` option. Set the ``namespace`` option at
initialization or manage it at runtime with
``AppEnlight.[set|clear]GlobalNamespace``::

    AppEnlight.init({
        apiKey: 'PUBLIC_API_KEY',
        namespace: 'my_script'
    });
    // OR
    AppEnlight.setGlobalNamespace('my_script');


**Tags and Extra**

Tags and extra can be specified globally or on the individual ``log`` and
``grabError`` level::

    AppEnlight.addGlobalTags({ widget: 'A', mobile: true });
    AppEnlight.log('info', undefined, undefined, { widget: 'B', button: 'send' });
    // Log will include the tags mobile: true, widget: 'B', button: 'send'

    try{
      1 + non_existing_var;
    }catch(exc){
      AppEnlight.grabError(exc, { tags: { widget: 'B' } });
    }


If a key already exists its value will be overridden::

    AppEnlight.addGlobalTags({ widget: 'A' });
    AppEnlight.addGlobalTags({ widget: 'B' });
    // Logs and reports will send the tag widget: 'B'


Use ``clearGlobal[Tags|Extra]`` to remove keys and their corresponding values.
Individual keys and values can be removed by passing an array with the keys to
remove::

    AppEnlight.clearGlobalTags([ 'widget' ]); // Remove only the widget key
    AppEnlight.clearGlobalExtra();            // Remove all keys and values

## Example AngularJS client integration and exception handling

You can easly connect your angular application with AppEnlight by decorating
$exceptionHandler decoration.

    ::javascript
    app.config(function($provide) {
        $provide.decorator("$exceptionHandler", function($delegate) {
            return function(exception, cause) {
                $delegate(exception, cause);
                if (typeof AppEnlight != 'undefined'){
                    AppEnlight.grabError(exception);
                }
            };
        });
    });

