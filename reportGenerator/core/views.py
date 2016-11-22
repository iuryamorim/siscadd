from django.http import HttpResponseRedirect
from django.shortcuts import resolve_url as r


def home(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(r('login:login'))
    return HttpResponseRedirect(r('report:report'))