from django.contrib import admin

from .models import SubSection, ServiceOffering, Service, Section


class SubSectionAdmin(admin.TabularInline):
    model = SubSection
    readonly_fields = ['section_icon_preview']


class SectionAdmin(admin.ModelAdmin):
    readonly_fields = ['section_image_preview']
    inlines = [SubSectionAdmin]
    list_display = ['title', 'created_on']
    search_fields = ['title']
    list_filter = ['title', 'section_type']


class ServiceAdmin(admin.ModelAdmin):
    readonly_fields = ['image_preview']
    # prepopulating slug from title
    prepopulated_fields = {'slug': ['name']}
    list_display = ['name', 'created_on']
    search_fields = ['name']
    list_filter = ['name']


class ServiceOfferingAdmin(admin.ModelAdmin):
    readonly_fields = ['icon_preview']
    list_display = ['title', 'created_on', ]
    search_fields = ['title']
    list_filter = ['title']


admin.site.register(Service, ServiceAdmin)
admin.site.register(ServiceOffering, ServiceOfferingAdmin)
admin.site.register(Section, SectionAdmin)

