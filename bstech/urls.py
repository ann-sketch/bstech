from django.contrib import admin
from django.urls import path,  include
from .views import (
    home_view,
    safoa_view,
    condom_view,
    eye_view,
    signup_view,
)

urlpatterns = [
    path('', home_view, name='home'),
    path('safoa/', safoa_view, name='safoa'),
    path('condom/', condom_view, name='condom'),
    path('eye/', eye_view, name='eye'),
    path('register/', signup_view, name='register'),
    path('', include('app.urls')),
    path('admin/', admin.site.urls),
]
