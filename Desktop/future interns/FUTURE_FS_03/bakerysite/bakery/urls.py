from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('menu/', views.menu, name='menu'),
    path('order/', views.order, name='order'),
    path('contact/', views.contact, name='contact'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart, name='cart'),
    path('remove/<int:item_id>/', views.remove_item, name='remove_item'),
]