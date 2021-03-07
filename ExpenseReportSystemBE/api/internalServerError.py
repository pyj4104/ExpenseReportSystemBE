from pyramid.view import exception_view_config
from pyramid.response import Response

@exception_view_config()
def internal_error(request):
    response =  Response('Internal error')
    response.status_int = 500
    return response
