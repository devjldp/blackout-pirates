from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm
# Create your views here.


def checkout(request):
    basket = request.session.get('basket', {})
    if not basket:
        messages.error()
        return redirect(reverse('concerts'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51PXpZKRur0OhULbvmPpuXKH0TfprzG2rlJxoa1fss3wbt8kYqi4WVPCYSOuoqgHbnJZIxfQIBpCjiGO7qj0I4jGA00p7wU63C6',
        'client_secret': 'test client secret' 
    }

    return render(request, template, context)
