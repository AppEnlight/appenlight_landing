Title: Tagging python logs and requests

# Tagging logs

Often you may want to tag your logs to carry additional information that you
can search later. For this, the python client uses the built in functionality of
the `extra` keyword used by python's logging framework.

    ::python
    log.warning('test message', extra={"action":'purchase', "price":17})

Those tags will appear in the log view above log messages. The client will send
dates, integers, and floats unchanged; every other value will be converted
to a string representation.

# Tagging requests

Additionally you can also tag requests themselves to carry additional searchable
information when exception or slowness reports are generated.

    ::python
    # inside your view function
    def some_view(request):
        request.environ['appenlight.tags']['type'] = 'cheat_attempt'
        request.environ['appenlight.tags']['count'] = 5
        ....
        return ...

When a new report is generated, the client will pass that data from the environ
as tags that are indexed and searchable in the AppEnlight interface.
