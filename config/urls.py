from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("profile_/", include('apps.profile_.urls')),
    path("nutition_api/", include('apps.users_.urls')),
    path('', include('apps.home.urls')),
    path("", include('theme_material_kit.urls')),

]
