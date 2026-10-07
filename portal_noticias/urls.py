from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("cuentas/", include("django.contrib.auth.urls")),
    path("api/", include("noticias.api_urls")),
    path("", include("noticias.urls")),
]
