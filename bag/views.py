from django.shortcuts import render, redirect

# Create your views here.


def view_bag(request):
    """A view to shows the shopping bag contents page"""
    return render(request, 'bag/bag.html')


def add_to_bag(request, product_id):
    """ Add a quantity of the specified product to the shopping bag """

    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if product_id in list(bag.keys()):
        bag[product_id] += quantity
    else:
        bag[product_id] = quantity

    request.session['bag'] = bag
    return redirect(request.POST.get('redirect_url'))
