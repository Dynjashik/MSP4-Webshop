from django.contrib import admin
from .models import UserProfile

# Register your models here.


class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'default_first_name',
        'default_last_name',
        'default_email',
        'default_phone_number',
        'default_street_address1',
        'default_street_address2',
        'default_town_or_city',
        'default_county',
        'default_postcode',
        'default_country'
    )


admin.site.register(UserProfile, UserProfileAdmin)
