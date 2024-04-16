from django.contrib import admin
from django.urls import path
from wallpaper_calculator.views import calculate_wallpaper

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', calculate_wallpaper, name='calculate_wallpaper'),
]
