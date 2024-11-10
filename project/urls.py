from django.contrib import admin
from django.urls import path, include
from debug_toolbar import urls as debug_toolbar_urls
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    # django allauth
    path("accounts/", include("allauth.urls")),
    # reload browser
    path("__reload__/", include("django_browser_reload.urls")),
    # apps
    path("", include("sample_app.urls")),
]

# Add debug toolbar urls
if settings.DEBUG:
    urlpatterns += [path("__debug__/", include(debug_toolbar_urls))]
