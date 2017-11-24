from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect

try:
    from django.utils.deprecation import MiddlewareMixin  # Django 1.10.x
except ImportError:
    MiddlewareMixin = object  # Django 1.4.x - Django 1.9.x


class SimpleMiddleware(MiddlewareMixin):

    def process_request(self, request):
        if str(request.path).index("/oa/"):
            if request.path == "/oa/login/":
                pass
            elif request.path == "/oa/loginAction/":
                pass
            elif request.path == "/oa/callback/":
                pass
            elif request.path == "/oa/index/":
                pass
            else:
                if request.session.get('session',None):
                    pass
                else:
                    return HttpResponseRedirect('/oa/login/')
        else:
            pass


