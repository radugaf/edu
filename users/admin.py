from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from users.models import UserAccount


class UserAccountAdmin(admin.ModelAdmin):
    list_display = ("email", "is_active", "is_staff", "is_superuser")
    list_filter = ("is_active", "is_staff", "is_superuser")


class UserAccountAdmin(BaseUserAdmin):
    ordering = ['email']
    list_display = ['email', 'first_name', 'last_name']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Teacher', {'fields': ('is_teacher',)}),
        ('Student', {'fields': ('is_student',)}),
    )

    # NOTE: Previous code was wrong.
    add_fieldsets = ((None, {'classes': ('wide',), 'fields': ('email', 'first_name', 'last_name', 'password1', 'password2')}),)


class UserInvitationAdmin(admin.ModelAdmin):
    list_display = ("user", "invitation_succeeded", "email", "phone_number")
    list_filter = ("invitation_succeeded",)


admin.site.register(UserAccount, UserAccountAdmin)
