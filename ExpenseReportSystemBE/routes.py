from ExpenseReportSystemBE.constants.services import SERVICES
from ExpenseReportSystemBE.constants.routes import ROUTES

def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    for service in SERVICES:
	    config.add_route(service, ROUTES[service])
