from django.urls import include, path

from apps.veterinaria import admin
from django.contrib import admin

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include('apps.veterinaria.urls'))
]
