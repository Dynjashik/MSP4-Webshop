from django.contrib import admin
from .models import News

# Register your models here.

class NewsAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'date_added',
        'description',
        'image',
        'image_url'
    )

    ordering = ('date_added',)

admin.site.register(News, NewsAdmin)
