Title: TurboGears2 exception logging and performance monitoring

# TurboGears2 exception logging and performance monitoring

*(This guide was created by Alessandro Molina - Thank you!)*

Approx. integration time: **2 minutes**

WSGI middleware is the most common way to use AppEnlight with your web application
written in the TurboGears2 web framework.

## Installation and Setup

Install the `appenlight_client` using pip:

    pip install appenlight-client

-----

## Example integration

Next you will want to ensure that the AppEnlight middleware is in place and
that the routing information is correctly reported.
To do so, edit `config/app_cfg.py`:

    ::python
    class AppEnlightSupport(object):
      def __call__(self):
          from tg import hooks
          hooks.register('before_config', self.enable_middleware)
          hooks.wrap_controller(self.enable_controller_wrapper)

      def enable_middleware(self, app):
          from tg import config
          from appenlight_client import make_appenlight_middleware
          return make_appenlight_middleware(app, config._current_obj())

      def enable_controller_wrapper(self, next_caller):
          from tg import request
          from appenlight_client.utils import fullyQualifiedName
          def appenlight_app_wrapper(config, controller, remainder, params):
              try:
                  controller_repr = fullyQualifiedName(controller)
              except:
                  controller_repr = repr(controller)
              request.environ['appenlight.view_name'] = controller_repr
              return next_caller(config, controller, remainder, params)
          return appenlight_app_wrapper


    from tg.configuration import milestones
    milestones.config_ready.register(AppEnlightSupport())

Now run your application providing the `APPENLIGHT_KEY/APPENLIGHT_INI`
environment variable, or you can add the `appenlight.api_key` to your
TurboGears2 .ini config file instead:

    ::ini
    appenlight.api_key = YOUR_PRIVATE_KEY
    # or use path ini file if you want to provide separate configuration
    appenlight.config_path = %(here)s/appenlight.ini
  
You can now run your instrumented application.
