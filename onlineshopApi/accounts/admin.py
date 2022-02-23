from django.contrib import admin
from .models import (
    BaseUser,
    Profile,
    Address,
)


# Register your models here.
# @admin.register(BaseUser)
class BaseUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'age']
    list_filter = ['username', 'age']
    list_per_page = 5
    ordering = ['first_name']


admin.site.register(BaseUser, BaseUserAdmin)


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone', 'gender']


admin.site.register(Profile, ProfileAdmin)


class AddressAdmin(admin.ModelAdmin):
    list_display = ['profile', 'date_created']
    list_filter = ['region', 'city', 'district']
    list_per_page = 5


admin.site.register(Address, AddressAdmin)
