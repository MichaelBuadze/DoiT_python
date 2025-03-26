from django.urls import path
from . import views

urlpatterns = [
    path('', views.dish_list, name='dish_list'),
    path('cart/', views.cart, name='cart'),
    path('add_to_cart/<int:dish_id>/', views.add_to_cart, name='add_to_cart'),
    path('update_cart/<int:dish_id>/<int:quantity>/', views.update_cart, name='update_cart'),
    path('remove_from_cart/<int:dish_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('register/', views.register, name='register'),
]