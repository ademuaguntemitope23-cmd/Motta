
from django.contrib import admin
from django.urls import path
from .views import social_apps

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", social_apps, name="home"),      # 👈 homepage
    path("social-apps/", social_apps, name="index"),
]
