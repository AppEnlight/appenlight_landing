Title: Django exception logging and performance monitoring

# Django exception logging and performance monitoring

![Django Logo](/static/images/logos/django_small.png)

Approx. integration time: **2 minutes**

Django middleware is the most common way to use AppEnlight with your
django framework web application.

## Installation and Setup

Install the `appenlight_client` using pip:

    pip install appenlight-client

-----

One of the more common ways to integrate your django application is
to add compatible middleware into your app.

Modify your settings file to contain this example configuration:

    ::python
    import appenlight_client.client as e_client
    APPENLIGHT = e_client.get_config({'appenlight.api_key':'YOUR_PRIVATE_KEY'})


You can also set `'appenlight.transport_config': 'https://self-hosted-appenlight.com'`
to configure the client to use your self-hosted AppEnlight instance.

Additionally, the middleware stack needs to be modified with an additional entry:
Please note that AppEnlight middleware should be first in the stack to
ensure that it functions properly.

    ::python
    MIDDLEWARE_CLASSES = (
        'appenlight_client.django_middleware.AppenlightMiddleware',
        'django.middleware.common.CommonMiddleware',
        ...




!!! note "Configuration via ini files/environ"

    You can set the `APPENLIGHT_KEY/APPENLIGHT_INI` environment variable instead;
    the client will try to load the configuration file from the absolute path or
    just use the key if it finds it in the environ.
