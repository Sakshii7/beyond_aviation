from django.contrib import admin

from .models import *


class ServiceAdmin(admin.ModelAdmin):
    readonly_fields = ['image_preview']


class ServiceOfferingAdmin(admin.ModelAdmin):
    readonly_fields = ['icon_preview']


class SectionAdmin(admin.ModelAdmin):
    readonly_fields = ['section_image_preview']


class SectionIconAdmin(admin.ModelAdmin):
    readonly_fields = ['section_icon_preview']


admin.site.register(Service, ServiceAdmin)
admin.site.register(ServiceOffering, ServiceOfferingAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(SubSection, SectionIconAdmin)
