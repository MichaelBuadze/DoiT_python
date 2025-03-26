from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Dish, Category
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dish_list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})



def dish_list(request):
    categories = Category.objects.all()
    dishes = Dish.objects.all()

    # ფილტრაცია
    category_filter = request.GET.get('category')
    if category_filter:
        dishes = dishes.filter(category__name=category_filter)

    spiciness_filter = request.GET.get('spiciness')
    if spiciness_filter:
        dishes = dishes.filter(spiciness=spiciness_filter)

    has_nuts_filter = request.GET.get('has_nuts')
    if has_nuts_filter:
        dishes = dishes.filter(has_nuts=has_nuts_filter == 'on')

    is_vegetarian_filter = request.GET.get('is_vegetarian')
    if is_vegetarian_filter:
        dishes = dishes.filter(is_vegetarian=is_vegetarian_filter == 'on')

    return render(request, 'restaurant/dish_list.html', {'dishes': dishes, 'categories': categories})

def add_to_cart(request, dish_id):
    dish = Dish.objects.get(pk=dish_id)
    cart = request.session.get('cart', [])
    item_exists = False

    for item in cart:
        if item['id'] == dish_id:
            item['quantity'] += 1
            item_exists = True
            break

    if not item_exists:
        cart.append({
            'id': dish.id,
            'name': dish.name,
            'price': float(dish.price),
            'quantity': 1,
            'image_url': dish.image.url,
        })

    request.session['cart'] = cart
    return redirect('dish_list')


@login_required
def cart(request):
    cart_items = request.session.get('cart', [])
    total_price = sum(item['price'] * item['quantity'] for item in cart_items)
    return render(request, 'restaurant/cart.html', {'cart_items': cart_items, 'total_price': total_price})

def update_cart(request, dish_id, quantity):
    if request.method == 'POST':  # დამატებულია შემოწმება
        cart = request.session.get('cart', [])
        for item in cart:
            if item['id'] == dish_id:
                new_quantity = int(request.POST.get('quantity')) # მიღებულია POST მონაცემები
                item['quantity'] = new_quantity
                if item['quantity'] <= 0:
                    cart.remove(item)
                break
        request.session['cart'] = cart
    return redirect('cart')

def remove_from_cart(request, dish_id):
  cart = request.session.get('cart', [])
  for item in cart:
    if item['id'] == dish_id:
      cart.remove(item)
      break
  request.session['cart'] = cart
  return redirect('cart')