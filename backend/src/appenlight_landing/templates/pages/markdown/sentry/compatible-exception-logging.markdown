Title: Sentry-compatible endpoint for exception reporting and logging

# Sentry-compatible endpoint for exception reporting and logging

![Ruby Logo](/static/images/logos/ruby_small.png) ![Javascript Logo](/static/images/logos/js_small.png) ![Node.js](/static/images/logos/nodejs.png) ![PHP Logo](/static/images/logos/php_small.png)

!!! note "Beta functionality"
    This feature is currently being tested in production. It is possible
    that there may be some bugs that we will fix as soon as possible when
    discovered.

We provide an endpoint compatible with `Sentry protocol API` in versions 6 and 7.
If you want to try out AppEnlight and you are currently using a Sentry client,
the easiest way to start is to just redirect your reports to our domain.

The system will automatically convert events into log entries or reports based
on their contents.

**Many users successfully use python and java clients with our service.**

To use the clients with AppEnlight, you need to change your `DSN`, to point
to new location:

    ::python
    DSN = https://APPENLIGHT_API_KEY:any_string@api.appenlight.com/sentry

Examples of clients and languages supported by the API:

* **Python**
* **JavaScript**
* **Node.js**
* **PHP**
* **Ruby**
* **Objective-C**
* **Java**
* **C#**
* **Go**
* **Perl**
* **ActionScript**
