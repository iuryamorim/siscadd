from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render, resolve_url as r

from reportGenerator.login.forms import LoginForm


def new(request):
    if not request.user.is_authenticated():
        if request.method == 'POST':
            return create(request)
        return empty_form(request)
    else:
        return call_redirect(request)


def create(request):
    form = LoginForm(request.POST)

    if not form.is_valid():
        return render(request, 'login/login.html', {'form': form})

    user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])

    if user is not None:
        login(request, user)
        return call_redirect(request)
    else:
        return render(request, 'login/login.html', {'form': form})


def empty_form(request):
    return render(request, 'login/login.html', {'form': LoginForm()})


def call_redirect(request):
    return HttpResponseRedirect(r('report:report'))


def call_logout(request):
    logout(request)
    return HttpResponseRedirect(r('login:login'))