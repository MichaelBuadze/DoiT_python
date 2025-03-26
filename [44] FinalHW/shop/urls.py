from django.urls import path
from .views import home, product_detail, add_to_cart, cart_view, remove_from_cart


urlpatterns = [
    path("", home, name="home"),
    path("product/<int:product_id>/", product_detail, name="product_detail"),
    path("cart/", cart_view, name="cart_view"),
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path("cart/remove/<int:cart_id>/", remove_from_cart, name="remove_from_cart"),
   
]