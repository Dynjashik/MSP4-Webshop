from django import forms
from .models import Contact


# Contact Form
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        """
        Adds placeholders and classes
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'name': 'Name',
            'email': 'Email Address',
            'subject': 'Subject',
            'message': 'Message',
        }

        self.fields['name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            placeholder = f'{placeholders[field]} *'
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'input-shadow'
            self.fields[field].label = False
