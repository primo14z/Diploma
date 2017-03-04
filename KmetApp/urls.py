from django.conf.urls import url, include
from django.contrib import admin

from . import views


app_name = 'KmetApp'

urlpatterns = [
    url(r'^home/', views.home, name='home'),
    url(r'^register_user/', views.register_user, name='register_user'),
    url(r'^logon/', views.logon, name='logon'),
    url(r'^logoff/', views.logoff, name='logoff'),
    url(r'^add_selling/', views.add_selling, name='add_selling'),
    url(r'^selling/', views.selling, name='selling'),
    url(r'^edit_user/', views.edit_user, name='edit_user'),
]