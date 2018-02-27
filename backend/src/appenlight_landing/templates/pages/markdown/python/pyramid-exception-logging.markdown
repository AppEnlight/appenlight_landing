Title: Pyramid exception logging and performance monitoring

# Pyramid exception logging and performance monitoring

![Pyramid Logo](/static/images/logos/pyramid_small.png)

Approx. integration time: **2 minutes**

WSGI middleware is the most common way to use AppEnlight with your web application
written in commonly used python web frameworks like **Pyramid, Zope2, repoze.bfg**.

## Installation and Setup

Install the `appenlight_client` using pip:

    pip install appenlight-client

-----

## Example integration

One of the more common ways to integrate your application is to add our client
directly into the WSGI pipeline.

In your INI file, you need to add:

    ::ini
    [filter:appenlight_client]
    use = egg:appenlight_client
    appenlight.api_key = YOUR_PRIVATE_KEY
    # appenlight.transport_config = https://self-hosted-appenlight.com #optional if you use the hosted version of App Enlight
    # appenlight.config_path is optional if you want to configure client via ini file
    appenlight.config_path = %(here)s/appenlight.ini

    [pipeline:main]
    pipeline =
        .....your other pipeline entries ....
        appenlight_client
        app_name

You also need to add *appenlight tween* to your application. You can do this in
two ways:

    ::python
    # by adding following line to your config object
    config.include('appenlight_client.ext.pyramid_tween')
    
Or by altering your ini file to contain a new include:

    ::ini
    pyramid.includes = appenlight_client.ext.pyramid_tween
                       ... other includes you might have ...
       
At this point everything should be ready, but in some cases you may not have 
explictly configured the WSGI pipeline inside of your ini file.


----

Changing the default scaffold configuration in Pyramid Web Framework
====================================================================

Default scaffolds in pyramid 1.3+ have a section called *[app:main]* -
the AppEnlight client expects that you are using *wsgi pipeline* instead to
position itself in it.

The easiest way to accomplish that is to alter your configuration file to look 
like this:

    ::ini
    # on line 1 of your ini file
    [app:main] becomes [app:yourappname] 

and inside your configuration, **above [server:main]** directive following 
directive should appear:

    ::ini
    [pipeline:main]
    pipeline =
        ... other middleware ...
        appenlight_client
        yourappname


Now you have explictly configured the pipeline with the client in it, ready to
stream information.

!!! note "Legacy applications/Import order issues"
    A custom pserver may be only required for older framework versions. 1.6 and
    above are usually fine to run with the default framework supplied command.

Running pyramid applications with custom `pserve` :

    APPENLIGHT_INI="/abs/path/to/appenlight.ini" appenlight_client pserve ...


