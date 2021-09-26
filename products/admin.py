from django.contrib import admin
from .models import Product, SkillCategory, EnvCategory

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'price',
        'skill_category',
        'env_category',
        'image',
        'image_url'
    )

    ordering = ('name',)

class SkillCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

class EnvCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

admin.site.register(Product, ProductAdmin)
admin.site.register(SkillCategory, SkillCategoryAdmin)
admin.site.register(EnvCategory, EnvCategoryAdmin)
