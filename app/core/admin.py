from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _

from core import models


class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'name']
    fieldsets = (
        (None, {
            'fields': (
                'email',
                'password'
            )
        }),
        (_('Personal Info'), {
            'fields': (
                'name',
                'phone_number',
                'address_1',
                'address_2',
                'city',
                'zipcode',
                'state',
            )
        }),
        (_('Permissions'), {
            'fields': (
                'is_active',
                'is_staff',
                'is_superuser',
                'token_oneinc',
            )
        }),
        (_('Important dates'), {
            'fields': (
                'last_login',
            )
        }),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email',
                'password1',
                'password2'
            )
        }),
    )


# Register our useradamin to the admin
admin.site.register(models.User, UserAdmin)
# Register our Quote to the admin
admin.site.register(models.Quote)
# # Register our Policy to the admin
admin.site.register(models.Policy)
# # Register our PaymentListMonth to the admin
admin.site.register(models.PaymentListMonth)
