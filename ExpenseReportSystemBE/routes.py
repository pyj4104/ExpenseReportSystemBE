from constants.services import SERVICES
from constants.routes import ROUTES

def includeme(config):
    for service in ROUTES:
	    config.add_route(service, ROUTES[service])
