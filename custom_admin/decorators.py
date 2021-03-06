from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import redirect
from django.contrib import messages


def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('custom_admin:index')
        else:
            return view_func(request, *args, **kwargs)
        return view_func(request, *args, **kwargs)
    return wrapper_func
    

def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            group = None
            if request.user.groups.exists() :
                group = request.user.groups.all()[0].name

            if group in allowed_roles or request.user.is_superuser:
                return view_func(request, *args, **kwargs)
            else:
                raise Http404

                # return HttpResponse('you are not ')

        return wrapper_func
    return decorator
