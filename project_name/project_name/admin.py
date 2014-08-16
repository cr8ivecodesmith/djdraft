from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import UserProfile


# Define inline profile models
class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'User profile'
    verbose_name = 'User profile'
    max_num = 1


# Register inline models with the user admin form
class UserAdmin(UserAdmin):
    inlines = (
        UserProfileInline,
    )


# Re-register the user admin form
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
