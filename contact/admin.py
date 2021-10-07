from django.contrib import admin
from .models import Contact

# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'user_profile',
        'email',
        'subject',
        'message',
        'date_sent'
    )

    ordering = ('date_sent',)


admin.site.register(Contact, ContactAdmin)
