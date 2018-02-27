Title: Python WSGI exception logging and performance monitoring

# Python WSGI exception logging and performance monitoring

![Python Logo](/static/images/logos/python_small.png)

Approx. integration time: **5 minutes**

WSGI middleware is the most common way to use AppEnlight with your web application
written in some of commonly used python web frameworks like **Pyramid, Zope2, repoze.bfg**.

## Installation and Setup


Install the ``appenlight_client`` using pip:

    pip install appenlight-client

-----

## Example integration

One of more common ways to integrate your application is to add
your client directly into WSGI pipeline.

First [**generate configuration file for the client**](/page/python/client-configuration).


To minimize configuration complexity, the client will default to looking for the
APPENLIGHT_INI environment variable that will supply the absolute path
to the config file.

Example for uWSGI:

    APPENLIGHT_INI="/abs/path/to/appenlight.ini" uwsgi --enable-threads ...
    # you could also use APPENLIGHT_KEY if you don't want to use an ini file for configuration control


This is the recommended method to configure the client. You can use some
alternative methods to configure the client if they better fit your environment.

* You can pass the config dictionary directly to the `client/make_middleware()` func
* Add client middleware directly in your wsgi.py file
* You can use the `appenlight_client.client.get_config()` utility function to
  load and parse the ini file.

Example:

    ::python
    import appenlight_client.client as e_client
    config = e_client.get_config({'appenlight.api_key':'YOUR_PRIVATE_KEY'})
    appenlight_client = e_client.Client(config)

This is particularly handy for tracking non-webapp code like celery tasks.

If you need to **wrap your WSGI application** after you get the config object with
`get_config` function, you can wrap your WSGI application yourself:

    ::python
    app = some_wsgi_function()
    app = e_client.make_appenlight_middleware(app, config)
    return app

Alternately, you can use decorator:

    ::python
    from appenlight_client import client

    @client.decorate()
    def application(environ, start_response):
        ...

Consult our documentation for popular python web frameworks for
general implementation ideas.
