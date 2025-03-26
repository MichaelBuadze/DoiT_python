from django.shortcuts import redirect, get_object_or_404
from shop.models import Product
from django.shortcuts import render
from shop.models import Product 
from django.shortcuts import redirect
from .models import Cart

def home(request):
    products = Product.objects.all()
    return render(request, "shop/home.html", {"products": products})

def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, "shop/product_detail.html", {"product": product})

def add_to_cart(request, product_id):
    if request.method == "POST":
        product = get_object_or_404(Product, id=product_id)
        cart = request.session.get('cart', [])
        cart.append(product_id)
        request.session['cart'] = cart
        return redirect('home')  # მთავარი გვერდზე დაბრუნება

def cart_view(request):
    cart_items = Cart.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, "shop/cart.html", {"cart_items": cart_items, "total_price": total_price})

def remove_from_cart(request, cart_id):
    Cart.objects.get(id=cart_id).delete()
    return redirect("cart_view")

