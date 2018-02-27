Title: Airbrake-compatible endpoint for exception logging

# Airbrake-compatible endpoint for exception logging

![Ruby Logo](/static/images/logos/ruby_small.png) ![Javascript Logo](/static/images/logos/js_small.png) ![Node.js](/static/images/logos/nodejs.png) ![PHP Logo](/static/images/logos/php_small.png)

We provide an endpoint compatible with `Airbrake Notice API` in version 2.2+,
if you want to try out AppEnlight and you are currently using a ruby gem for Airbrake
(or any compatible client that uses the Airbrake protocol), the easiest way to start
is to just redirect your reports to our domain.

**Many users successfully use Rails and JavaScript clients with our service.**

As an example, for applications using `airbrake gem`, first you need to open
`config/initializers/airbrake.rb` inside your application and change your config
to:

    ::ruby
    Airbrake.configure do |config|
      config.api_key = 'ERRORMATOR_PRIVATE_API_KEY'
      config.host = 'api.appenlight.com'
      config.secure = true
    end

Currently *only XML* payloads are supported.
