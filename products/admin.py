from django.contrib import admin
from .models import Product, SkillCategory, EnvCategory

# Register your models here.
admin.site.register(Product)
admin.site.register(SkillCategory)
admin.site.register(EnvCategory)
