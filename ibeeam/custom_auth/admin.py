from django.contrib import admin

from custom_auth.models import User
from main.admin import ibeeam_site


class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ('profile_id',)


ibeeam_site.register(User, UserAdmin)
