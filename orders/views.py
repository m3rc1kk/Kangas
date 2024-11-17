from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView
from .models import Order, OrderItem
from .forms import OrderForm
from cart.cart import Cart


@login_required
def order_create(request):
    cart = Cart(request.user)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            for item in cart:

                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'],
                                         size = item['size'])


            cart.clear()
            request.session['order_id']=order.id

            return redirect(reverse('payment:process'))

    else:
        form = OrderForm(initial={
            'first_name': request.user.first_name or '',
            'last_name': request.user.last_name or '',
            'email': request.user.email or '',
            'city': request.user.city or '',
        })

    return render(request, 'orders/order/create.html', {'cart': cart, 'form': form})


class OrderListView(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'orders/order_list.html'
    context_object_name = 'orders'

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user).order_by('-created')