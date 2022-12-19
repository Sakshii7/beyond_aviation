from beyond_aviation.settings import MEDIA_URL
from django.contrib import admin
from django.db import models
from django.shortcuts import redirect
from tinymce.widgets import TinyMCE

from .models import SubSection, ServiceOffering, Service, Section, Menu, Page, QueryForm, Setting


class SubSectionAdmin(admin.TabularInline):
    model = SubSection
    list_editable = ['status']
    readonly_fields = ['section_icon_preview']


class SectionAdmin(admin.ModelAdmin):
    readonly_fields = ['section_image_preview']
    inlines = [SubSectionAdmin]
    list_display = ['title', 'created_on', 'status']
    search_fields = ['title']
    list_filter = ['title', 'section_type']
    list_editable = ['status']
    list_per_page = 5


class ServiceAdmin(admin.ModelAdmin):
    readonly_fields = ['image_preview']
    # prepopulating slug from title
    prepopulated_fields = {'slug': ['name']}
    list_display = ['name', 'created_on', 'status']
    search_fields = ['name']
    list_filter = ['name']
    list_editable = ['status']
    list_per_page = 5
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }


class ServiceOfferingAdmin(admin.ModelAdmin):
    readonly_fields = ['icon_preview']
    list_display = ['title', 'created_on', 'status', ]
    search_fields = ['title']
    list_filter = ['title']
    list_editable = ['status']
    list_per_page = 5


class MenuAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['name']}
    list_display = ['name', 'created_on', 'status']
    search_fields = ['name']
    list_filter = ['name']
    list_editable = ['status']
    list_per_page = 5


class QueryFormAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'created_on']
    search_fields = ['first_name']
    list_filter = ['first_name']


class PageAdmin(admin.ModelAdmin):
    readonly_fields = ['logo_preview']
    list_display = ['title', 'created_on', 'status']
    prepopulated_fields = {'slug': ['title']}
    search_fields = ['title']
    # list_filter = ['title']
    list_editable = ['status']
    list_per_page = 5
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }


class SettingAdmin(admin.ModelAdmin):
    change_list_template = 'admin/change_list_custom.html'

    def has_add_permission(self, request) -> bool:
        return False

    def has_delete_permission(self, request, obj=None) -> bool:
        return False

    def has_change_permission(self, request, obj=None) -> bool:
        return False

    def changelist_view(self, request, extra_context=None):

        if request.method == 'POST':

            contact_address = request.POST['contact_address']
            facebook_url = request.POST['facebook_url']
            instagram_url = request.POST['instagram_url']
            twitter_url = request.POST['twitter_url']
            homepage_logo = request.FILES['homepage_logo']
            footer_logo = request.FILES['footer_logo']
            rows_count = Setting.objects.all().count()
            if rows_count != 0:
                settings = Setting.objects.get()
                settings.contact_address = contact_address
                settings.facebook_url = facebook_url
                settings.instagram_url = instagram_url
                settings.twitter_url = twitter_url
                settings.homepage_logo = request.FILES.get('homepage_logo')
                settings.footer_logo = request.FILES.get('footer_logo')
                # print(settings.footer_logo)
                settings.save()
            else:

                query_id = Setting(contact_address=contact_address, facebook_url=facebook_url,
                                   instagram_url=instagram_url, twitter_url=twitter_url, homepage_logo=homepage_logo,
                                   footer_logo=footer_logo)
                query_id.save()

            return redirect('/admin/homepage/setting/')

        settings = Setting.objects.all()
        if settings.count() == 0:
            settings = ""
        else:
            settings = settings[0]

        context = {
            "settings": settings,
            "media_url": MEDIA_URL
        }
        response = super().changelist_view(request, context)
        return response


admin.site.register(Service, ServiceAdmin)
admin.site.register(ServiceOffering, ServiceOfferingAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(Menu, MenuAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(QueryForm, QueryFormAdmin)
admin.site.register(Setting, SettingAdmin)
