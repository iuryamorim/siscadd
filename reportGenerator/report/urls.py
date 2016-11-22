from django.conf.urls import url

from reportGenerator.report.views import new

urlpatterns = [
    url(r'^$', new, name='report'),
]