from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51JTU0bLStlNmediIiws2Rl2Vu4giKbZ5j2tGI8BM6BOJsPZNxYLlho7KZNEy4RQHKYJBwLSkL3EaiqCX5UA9ffvu00YQJvGFMs',
        'client_secret': 'sk_test_51JTU0bLStlNmediInoGBuWUJ2F3WVzDyrSEcCs02ERXry5wc0eQpd9l1lUZ6E07z2FRMj5IcuxsIzlT6cMYTjPm300lbCl8nPP',
        }
    return render(request, template, context)
