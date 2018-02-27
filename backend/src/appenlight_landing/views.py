import logging
import markdown
import os
from pkg_resources import resource_exists, resource_isdir, resource_string
import webhelpers2.text

from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound, HTTPNotFound
from pyramid.security import NO_PERMISSION_REQUIRED
from pyramid.renderers import render_to_response

log = logging.getLogger(__name__)


@view_config(route_name='/', renderer='templates/index.jinja2')
def index(request):
    return {}

@view_config(route_name='plans', renderer='templates/default/plans.jinja2')
def plans(request):
    return {}

@view_config(route_name='pages', permission=NO_PERMISSION_REQUIRED)
def show_rest(request):
    """
    Renders RST pages for documentation
    """
    renderer = 'templates/pages/rest_page.jinja2'
    page_path = request.matchdict.get('page')
    clean_pages = ['credits', 'privacy-policy', 'terms-of-service']
    # use different template for doc pages
    if page_path and page_path[0] in clean_pages:
        renderer = 'templates/pages/rest_clean_page.jinja2'

    if not page_path:
        return HTTPFound(
                location=request.route_url('pages', page=('api', 'main')))

    # should be cached eventually
    def render_rst_page(page):
        page = '%s.markdown' % os.path.join(*page)
        resouce_path = os.path.join('templates/pages/markdown', page)
        exists = resource_exists('appenlight_landing', resouce_path)
        is_dir = resource_isdir('appenlight_landing', resouce_path)
        if exists and not is_dir:
            page_str = resource_string('appenlight_landing', resouce_path)
            md = markdown.Markdown(
                    extensions=['codehilite(guess_lang=False)',
                                'extra', 'admonition',
                                'headerid', 'meta'])
            body = md.convert(page_str.decode('utf8'))
        else:
            raise HTTPNotFound()
        return ' '.join(md.Meta.get('title', '')), body

    title, html_body = render_rst_page(page_path)
    to_renderer = {'html_body': html_body,
                   'title': title,
                   'content_class': webhelpers2.text.urlify(title)}

    return render_to_response(renderer, to_renderer, request)


@view_config(route_name='contact',
             renderer='templates/contact/unlogged.jinja2',
             permission=NO_PERMISSION_REQUIRED)
def contact_unlogged(request):
    return {'contact_form': None}


@view_config(route_name='features',
             renderer='templates/default/features.jinja2',
             permission=NO_PERMISSION_REQUIRED)
def features(request):
    """
    Renders features page
    """
    return {}
