import csv
from io import TextIOWrapper

from django.http import HttpResponseRedirect
from django.shortcuts import render, resolve_url as r

from reportGenerator.report.forms import ImportForm
from reportGenerator.report.src.main import Report


def new(request):
    if not request.user.is_authenticated():
        return call_login(request)
    else:
        return create(request)


def call_login(request):
    return HttpResponseRedirect(r('login:login'))


def create(request):
    if request.method == "POST":
        sigla = None
        form = ImportForm(request.POST, request.FILES)
        if not form.is_valid():
            return render(request, 'report/report.html', {'form': form})
        try:
            sigla = handle_files(request)
        except:
            return render(request, 'report/report.html', {'form': form, 'error': True})
        return render(request, 'report/success.html', {'sigla': sigla})
    return render(request, 'report/report.html', {'form': ImportForm()})


def handle_files(request):
    f = TextIOWrapper(request.FILES['file'].file, encoding='ascii', errors='replace')
    dic = csv.DictReader(f, delimiter=';')
    name = ''
    for d in dic:
        name = d['COD_CURSO']
        break

    Report.planilhas(dic, name, 'media', 2015, 2)

    return name

