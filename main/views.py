from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView

from account.forms import UserForm
from account.models import User
from cart.forms import CartAddProductForm
from main.models import Product


class ListProductView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'main/product_list.html'

class DetailProductView(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'main/product_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart_product_form'] = CartAddProductForm()
        return context

def add_favorite_product(request, product_id, product_slug):
    if request.method == 'POST':
        product = get_object_or_404(Product, id=product_id)

        if product not in request.user.favorites.all():
            request.user.favorites.add(product)
            return redirect('main:product-list')
        else:
            request.user.favorites.remove(product)
            return redirect('main:product-list')
    return redirect('main:product-detail', product_id, product_slug)

class FavoriteProductView(ListView):
    model = User
    context_object_name = 'user'
    template_name = 'main/favorites.html'