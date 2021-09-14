from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages
from products.models import Product


def view_bag(request):
    """A view to shows the shopping bag contents page"""
    return render(request, 'bag/bag.html')


def add_to_bag(request, product_id):
    """ Add a quantity of the specified product to the shopping bag """

    product = Product.objects.get(pk=product_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})
    if product_id in list(bag.keys()):
        bag[product_id] += quantity
    else:
        bag[product_id] = quantity

        messages.success(request, f'Added {product.name} to your bag')

    request.session['bag'] = bag

    redirect_url = request.POST.get('redirect_url')
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    quantity = int(request.POST.get('quantity'))

    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
    else:
        bag.pop(item_id)

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""

    try:
        bag = request.session.get('bag', {})
        bag.pop(item_id)
        request.session['bag'] = bag
        return HttpResponse(status=200)
    except Exception as e:
        return HttpResponse(status=500)
