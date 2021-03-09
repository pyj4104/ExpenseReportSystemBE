from pyramid.config import Configurator
from pyramid.session import SignedCookieSessionFactory
from ExpenseReportSystemBE.helpers.tokenGenerator import tokenGenerator as tg

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    with Configurator(settings=settings) as config:
        config.include('.routes')
        config.include('.models')
        config.include('pyramid_mailer')
        config.set_session_factory(SignedCookieSessionFactory(tg(64)))
        config.scan()
    return config.make_wsgi_app()
