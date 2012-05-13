from accounts.models import *
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin

class UserProfileInline(admin.TabularInline):
    model = UserProfile

class UserAdmin(DjangoUserAdmin):
    inlines = (UserProfileInline,)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Team)
admin.site.register(Player)