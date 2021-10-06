from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, EnvCategory, SkillCategory


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(label='Image',
                             required=False,
                             widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        skill_categories = SkillCategory.objects.all()
        skillnames = [(c.id, c.get_friendly_name()) for c in skill_categories]

        env_categories = EnvCategory.objects.all()
        envnames = [(c.id, c.get_friendly_name()) for c in env_categories]

        self.fields['skill_category'].choices = skillnames
        self.fields['env_category'].choices = envnames

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
