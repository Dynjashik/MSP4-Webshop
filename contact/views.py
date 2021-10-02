from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, redirect, reverse
from .models import Contact
from .forms import ContactForm


def add_contact_item(request):
    """ Add contact """

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Message sent successfully. Thank you for contacting us')
        else:
            messages.error(request, 'Message failed to send. Please check if the form is valid.')

    form = ContactForm()

    template = 'contact/contact.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
