from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm

from .models import CustomUser, Party, Gift, Guest


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeForm


@admin.register(Party)
class PartyAdmin(admin.ModelAdmin):
    readonly_fields = ("uuid",)


@admin.register(Gift)
class GiftAdmin(admin.ModelAdmin):
    readonly_fields = ("uuid",)


@admin.register(Guest)
class GuestAdmin(admin.ModelAdmin):
    readonly_fields = ("uuid",)
