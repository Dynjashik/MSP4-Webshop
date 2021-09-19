from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, EnvCategory, SkillCategory


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        skill_categories = SkillCategory.objects.all()
        skill_friendly_names = [(c.id, c.get_friendly_name()) for c in skill_categories]

        env_categories = EnvCategory.objects.all()
        env_friendly_names = [(c.id, c.get_friendly_name()) for c in env_categories]

        self.fields['skill_category'].choices = skill_friendly_names
        self.fields['env_category'].choices = env_friendly_names

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
