Title: Pylons exception logging and performance monitoring

# Pylons exception logging and performance monitoring

![Pyramid Logo](/static/images/logos/pylons_small.png)

Approx. integration time: **2 minutes**

WSGI middleware is the most common way to use AppEnlight with your Pylons
framework web application.

## Installation and Setup

Install the ``appenlight_client`` using pip:

    pip install appenlight-client

-----

One of the more common ways to integrate your application is to add
your client directly into the WSGI pipeline.

For the Pylons app, you need to modify config/middleware.py:

    ::python
    # CUSTOM MIDDLEWARE HERE (filtered by error handling middlewares)
    # find this line and below add
    
    from appenlight_client import make_appenlight_middleware
    app = make_appenlight_middleware(app, config)

Run your application providing the `APPENLIGHT_KEY/APPENLIGHT_INI` environment
variable, or you can add the `appenlight.api_key` to your pylons app config file
instead:

    ::ini
    appenlight.api_key = YOUR_PRIVATE_KEY
    # or use path ini file if you want to provide separate configuration
    appenlight.config_path = %(here)s/appenlight.ini

You can now run your instrumented application.
