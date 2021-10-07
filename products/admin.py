from django.contrib import admin
from .models import Product, SkillCategory, EnvCategory

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'description',
        'price',
        'skill_categories',
        'env_categories',
        'image',
        'image_url'
    )

    ordering = ('sku',)

    def skill_categories(self, obj):
        return "\n".join([p["name"] for p in obj.skill_category.values()])

    def env_categories(self, obj):
        return "\n".join([p["name"] for p in obj.env_category.values()])


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
