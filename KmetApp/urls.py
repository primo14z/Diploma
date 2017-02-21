from django.conf.urls import url, include
from django.contrib import admin
from . import views


app_name='KmetApp'

urlpatterns= [
    url(r'^home/', views.home, name='home'),
    url(r'^logIn/', views.logIn, name='logIn'),
    url(r'^registration/', views.registration, name='registration'),
    url(r'^register_user/', views.register_user, name='register_user'),
    url(r'^test/', views.test, name='test'),
    url(r'^testView/', views.testView, name='testView'),
]