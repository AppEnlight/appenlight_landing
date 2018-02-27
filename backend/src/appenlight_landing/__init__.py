from pyramid.config import Configurator


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('/', '/')
    config.add_route('features', '/features')
    config.add_route('pages', '/page/*page')
    config.add_route('welcome', '/welcome')
    config.add_route('plans', '/plans')
    config.add_route('contact', '/contact')
    config.scan()
    return config.make_wsgi_app()
