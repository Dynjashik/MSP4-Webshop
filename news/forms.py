from django import forms
from .widgets import CustomClearableFileInput
from .models import News


class NewsForm(forms.ModelForm):

    class Meta:
        model = News
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date_added'].widget.attrs['readonly'] = True
        for _, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
