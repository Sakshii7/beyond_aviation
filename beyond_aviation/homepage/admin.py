from django.contrib import admin

from .models import *


class ServiceAdmin(admin.ModelAdmin):
    readonly_fields = ['image_preview']


class ServiceOfferingAdmin(admin.ModelAdmin):
    readonly_fields = ['icon_preview']


admin.site.register(Service, ServiceAdmin)
admin.site.register(ServiceOffering, ServiceOfferingAdmin)
