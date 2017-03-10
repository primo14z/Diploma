from django.conf.urls import url

from . import views


app_name = 'KmetApp'

urlpatterns = [
    url(r'^home/', views.home, name='home'),
    url(r'^register_user/', views.register_user, name='register_user'),
    url(r'^logon/', views.logon, name='logon'),
    url(r'^logoff/', views.logoff, name='logoff'),
    url(r'^add_selling/', views.add_selling, name='add_selling'),
    url(r'^edit_user/', views.edit_user, name='edit_user'),
    url(r'^search_selling/', views.search_selling, name='search_selling'),
    url(r'^add_orderS/', views.add_orderS, name='add_orderS'),
    url(r'^my_sellings/', views.my_sellings, name='my_sellings'),
    url(r'^disable_selling/', views.disable_selling, name='disable_selling'),
    url(r'^add_basket/', views.add_basket, name='add_basket'),
    url(r'^search_basket/', views.search_basket, name='search_basket'),

]