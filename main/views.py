from django.shortcuts import render
from django.views.generic import ListView, DetailView

from main.models import Product


class ListProductView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'main/product_list.html'

class DetailProductView(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'main/product_detail.html'