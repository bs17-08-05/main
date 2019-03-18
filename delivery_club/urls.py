from core.admin import admin_site_reports
from django.urls import path, include


urlpatterns = [
    path('admin/', admin_site_reports.urls),
    path('api/', include('core.urls'))
]
