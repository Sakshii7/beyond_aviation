from django.contrib import admin

from .models import *


class SubSectionAdmin(admin.TabularInline):
    model = SubSection
    readonly_fields = ['section_icon_preview']


class SectionAdmin(admin.ModelAdmin):
    readonly_fields = ['section_image_preview']
    inlines = [SubSectionAdmin, ]


class ServiceAdmin(admin.ModelAdmin):
    readonly_fields = ['image_preview']


class ServiceOfferingAdmin(admin.ModelAdmin):
    readonly_fields = ['icon_preview']


admin.site.register(Service, ServiceAdmin)
admin.site.register(ServiceOffering, ServiceOfferingAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.site_header = "Go Above And Beyond"
admin.site.site_title = "Go Above And Beyond admin site"
admin.site.index_title = "Go Above And Beyond Admin"
