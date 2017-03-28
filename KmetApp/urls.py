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
    url(r'^my_OrderSellings/', views.my_OrderSellings, name='my_OrderSellings'),
    url(r'^undoneOrder/', views.undoneOrder, name='undoneOrder'),
    url(r'^doneOrder/', views.doneOrder, name='doneOrder'),
    url(r'^editSelling/', views.editSelling, name='editSelling'),
    url(r'^complete_orderSelling/', views.complete_orderSelling, name='complete_orderSelling'),
    url(r'^add_orderB/', views.add_orderB, name='add_orderB'),
    url(r'^disable_basket/', views.disable_basket, name='disable_basket'),
    url(r'^my_baskets/', views.my_baskets, name='my_baskets'),
    url(r'^editBasket/', views.editBasket, name='editBasket'),
    url(r'^my_OrderBasket/', views.my_OrderBasket, name='my_OrderBasket'),
    url(r'^undoneOrderB/', views.undoneOrderB, name='undoneOrderB'),
    url(r'^doneOrderB/', views.doneOrderB, name='doneOrderB'),
    url(r'^complete_orderBasket/', views.complete_orderBasket, name='complete_orderBasket'),
    


]