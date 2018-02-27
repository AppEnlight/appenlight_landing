Title: Manual logging and error handlers in applications

Timing your application code
----------------------------

Often you may want to time parts or libraries of your application that are not
handled automatically by our client.

For this case, the client provides an utility decorator called `time_trace`. You
can use it to decorate any callable in your application and it will appear on
your AppEnlight timeline and reports as a "custom" layer.

    ::python
    from appenlight_client.timing import time_trace

    @time_trace(name='namespace.foobar', min_duration=0.1)
    def foobar():
        time.sleep(0.12)
        return 1


Manual logging and error handlers in applications
-------------------------------------------------

Sometimes you might find that you need to log exceptions and other information
directly from your code and views.

Because of the nature of our client and the fact that it handles a lot more than
just exceptions, supports batching, and gathers performance metrics and other
state information, it provides a utility function `gather_data` for handling those
kinds of scenarios and checks the special environ key for traceback objects for
you to use.

Error handlers in frameworks
----------------------------

One of the situations where you might want to use it is when you use custom
error handlers that catch the exception before our WSGI middleware could handle
it. Here is an easy solution you can use to notify the middleware that something
went wrong.

In your view handler, place following code:

    ::python
    from appenlight_client.exceptions import get_current_traceback

    if 'appenlight.client' in request.environ:
        # pass the traceback object to middleware
        request.environ['appenlight.__traceback'] = get_current_traceback(
                skip=1,
                show_hidden_frames=True,
                ignore_system_exceptions=True)

`appenlight.__traceback` will now carry a traceback object that the client
middleware will pick up and process normally like any other unhandled exception.
Everything will be handled for you: logs, performance metrics, and request timing.
This is the most friction free approach to handle error handlers if our client
doesn't handle them out-of-the-box for you.

Sending data manually
---------------------

Another common scenario is when you want to send reports/logs manually to the service:

    ::python
    from appenlight_client.ext.general import gather_data
    gather_data(APPENLIGHT_CLIENT, request.environ)

`APPENLIGHT_CLIENT` is your client instance; it should be available to you as
`request.environ['appenlight.client']`.

`request.environ` can be substituted with a fake environ dictionary in the form
of `{'appenlight.view_name': 'view_name'}`.
By default, the client will gather the last exception in the system and all of
the log and slow call entries that qualify for submission.
Optionally, pass `start_time` and `end_time` if you want to see the execution
times of this report in your dashboard.

