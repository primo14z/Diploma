from django.conf.urls import url, include
from django.contrib import admin

from . import views


app_name = 'KmetApp'

urlpatterns = [
    url(r'^home/', views.home, name='home'),
    url(r'^register_user/', views.register_user, name='register_user'),
    url(r'^logon/', views.logon, name='logon'),
    url(r'^logoff/', views.logoff, name='logoff'),
]