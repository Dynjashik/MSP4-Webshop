from django.contrib import messages
from django.shortcuts import render
from profiles.models import UserProfile
from .forms import ContactForm


def add_contact_item(request):
    """ Add contact """

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            if request.user.is_authenticated:
                profile = UserProfile.objects.get(user=request.user)
                contact.user_profile = profile
            contact.save()
            messages.success(
                request,
                'Message sent successfully. Thank you for contacting us')
        else:
            messages.error(
                request,
                'Message failed to send. Please check if the form is valid.')

    form = ContactForm()
    template = 'contact/contact.html'
    context = {
        'form': form,
        'show_without_bag': True
    }
    return render(request, template, context)
