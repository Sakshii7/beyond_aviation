import json

from django import forms
from django.contrib import admin
from django.http import HttpResponse

from tinymce.widgets import TinyMCE
from django.db import models
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
    readonly_fields = ['logo_preview']
    # prepopulating slug from title
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
    list_display = ['title', 'created_on', 'status']
    prepopulated_fields = {'slug': ['title']}
    search_fields = ['title']
    list_filter = ['title']
    list_editable = ['status']
    list_per_page = 5
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }


class TestingForm(forms.Form):
    contact_address = forms.CharField()
    facebook_url = forms.URLField()
    instagram_url = forms.URLField()
    twitter_url = forms.URLField()


class SettingAdmin(admin.ModelAdmin):
    change_list_template = 'admin/change_list_custom.html'

    def has_add_permission(self, request) -> bool:
        return False

    def has_delete_permission(self, request, obj=None) -> bool:
        return False

    def has_change_permission(self, request, obj=None) -> bool:
        return False

    def changelist_view(self, request, extra_context=None):
        request_full_path = request.get_full_path()
        extra_context = {
            "form": TestingForm()
        }

        if request.method == 'POST':
            details = TestingForm(request.POST)
            extra_context['form'] = details
            if details.is_valid():
                contact_address = request.POST['contact_address']
                facebook_url = request.POST['facebook_url']
                instagram_url = request.POST['instagram_url']
                twitter_url = request.POST['twitter_url']
                if details:
                    system_data = Setting(contact_address=contact_address, facebook_url=facebook_url,
                                          instagram_url=instagram_url, twitter_url=twitter_url)
                    x = system_data.id
                    system_data.save()
                    detail_id = Setting.objects.get(id__isnull=False)
                    detail_id.contact_address = contact_address
                    detail_id.facebook_url = facebook_url
                    detail_id.instagram_url = instagram_url
                    detail_id.twitter_url = twitter_url
                    for res in detail_id:
                        res.save()
                    # detail_id.save()
                    print(detail_id.contact_address)
                    system_data.save()
                    response = super().changelist_view(request, extra_context)
                    return response
                else:

                    response = super().changelist_view(request, extra_context)
                    return response
            else:
                print('----------------NO----------------------')

        response = super().changelist_view(request, extra_context)
        return response


admin.site.register(Service, ServiceAdmin)
admin.site.register(ServiceOffering, ServiceOfferingAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(Menu, MenuAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(QueryForm, QueryFormAdmin)
admin.site.register(Setting, SettingAdmin)
