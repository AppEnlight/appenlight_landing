Title: Flask exception logging and performance monitoring

# Flask exception logging and performance monitoring

![Flask Logo](/static/images/logos/flask_small.png)

Approx. integration time: **2 minutes**

WSGI middleware is the most common way to use AppEnlight with your Flask
web application.

## Installation and Setup

Install the `appenlight_client` using pip:

    pip install appenlight-client blinker

-----  

Next you will need to add the AppEnlight WSGI middleware to the Flask pipeline:

    ::python
    app = Flask(__name__)
    import appenlight_client.ext.flask as appenlight
    app = appenlight.add_appenlight(app, {'appenlight.api_key':'YOUR_PRIVATE_KEY'})
    
**Your application should be configured for AppEnlight.**

You can also set `'appenlight.transport_config': 'https://self-hosted-appenlight.com'`
to configure the client to use your self-hosted AppEnlight instance.

## Tips & Tricks

There are alternative ways to tell the client what configuration options you want:

For example, you may want to pass the config via the APPENLIGHT_KEY/APPENLIGHT_INI
environment variable instead:

    ::python
    app = Flask(__name__)
    import appenlight_client.ext.flask as appenlight
    import appenlight_client.client as e_client
    config = e_client.get_config()
    app = appenlight.add_appenlight(app, config)

Now when you start your application, please add the following environment variable:

    APPENLIGHT_KEY="YOUR_PRIVATE_KEY" python flask_app.py
