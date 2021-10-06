from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import UserProfile
from .forms import UserProfileForm


@login_required
def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request,
                           """Update failed. Please ensure the form
                              is valid.""")
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)


@login_required
def order_history(request, order_number):
    profile = get_object_or_404(UserProfile, user=request.user)
    orders_found = profile.orders.filter(order_number=order_number)
    if orders_found:
        order = orders_found[0]
        messages.info(request, (
            f'This is a past confirmation for order number {order_number}.'
            'A confirmation email was sent on the order date.'
        ))

        template = 'checkout/checkout_success.html'
        context = {
            'order': order,
            'from_profile': True,
        }
    else:
        messages.warning(request,
                         (f"""Order {order_number} was not found in
                           your account."""))
        return redirect(reverse('home'))
    return render(request, template, context)
