from django.http import HttpResponseRedirect
from django.conf import settings


def login_middleware(get_response):
    def middleware(request):
        # before view
        if not (request.user.is_authenticated or '/admin/login/' in request.path):
            return HttpResponseRedirect(settings.LOGIN_URL)
        # if request.user.is_authenticated:
        #     return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)
        response = get_response(request)

        # after view

        return response

    return middleware
