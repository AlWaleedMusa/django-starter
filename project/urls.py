from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    # django allauth
    path("accounts/", include("allauth.urls")),
    # reload browser
    path("__reload__/", include("django_browser_reload.urls")),

    # sample_app
    path("", include("sample_app.urls")),
]
