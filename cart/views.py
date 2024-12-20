from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from main.models import Product
from .cart import Cart
from .forms import CartAddProductForm

@require_POST
@login_required
def cart_add(request, product_id, product_slug):
    cart = Cart(request.user)
    product = get_object_or_404(Product, id=product_id, slug=product_slug)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                override_quantity=cd['override'],
                 size=cd['size'])
    return redirect('cart:cart_detail')


@require_POST
@login_required
def cart_remove(request, product_id, product_slug, size):
    cart = Cart(request.user)
    product = get_object_or_404(Product, id=product_id, slug = product_slug)
    cart.remove(product, size)
    return redirect('cart:cart_detail')

@login_required
def cart_detail(request):
    cart = Cart(request.user)
    return render(request, 'cart/detail.html', {'cart': cart})