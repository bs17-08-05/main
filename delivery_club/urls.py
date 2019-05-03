from core.admin import admin_site_reports
from django.urls import path, include
from django.conf.urls.static import static

from . import settings


urlpatterns = [
    path('admin/', admin_site_reports.urls),
    path('api/courier/', include('courier_management.urls')),
    path('api/', include('core.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
