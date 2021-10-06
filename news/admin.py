from django.contrib import admin
from .models import News

# Register your models here.


class NewsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'date_added',
        'description',
        'image'
    )

    ordering = ('-date_added',)


admin.site.register(News, NewsAdmin)
