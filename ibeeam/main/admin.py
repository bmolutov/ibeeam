from django.contrib import admin
from django.contrib.auth.models import Group


class IbeeamAdminArea(admin.AdminSite):
    site_header = 'Ibeeam database'


ibeeam_site = IbeeamAdminArea(name='IbeeamAdmin')
admin.site.unregister(Group)
ibeeam_site.register(Group)
