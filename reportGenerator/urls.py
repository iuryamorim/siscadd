from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static

from reportGenerator.core.views import home

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^login/', include('reportGenerator.login.urls', namespace='login')),
    url(r'^report/', include('reportGenerator.report.urls', namespace='report')),

    url(r'^admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)