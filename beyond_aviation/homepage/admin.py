from django import forms
from django.contrib import admin

from .models import SubSection, ServiceOffering, Service, Section, Menu, Page, Contact


class SubSectionAdmin(admin.TabularInline):
    model = SubSection
    readonly_fields = ['section_icon_preview']


class SectionAdmin(admin.ModelAdmin):
    readonly_fields = ['section_image_preview']
    inlines = [SubSectionAdmin]
    list_display = ['title', 'created_on', 'status']
    search_fields = ['title']
    list_filter = ['title', 'section_type']


class ServiceAdmin(admin.ModelAdmin):
    readonly_fields = ['image_preview']
    # prepopulating slug from title
    prepopulated_fields = {'slug': ['name']}
    list_display = ['name', 'created_on', 'status']
    search_fields = ['name']
    list_filter = ['name']


class ServiceOfferingAdmin(admin.ModelAdmin):
    readonly_fields = ['icon_preview']
    list_display = ['title', 'created_on', 'status', ]
    search_fields = ['title']
    list_filter = ['title']


class MenuAdmin(admin.ModelAdmin):
    readonly_fields = ['logo_preview']
    # prepopulating slug from title
    prepopulated_fields = {'slug': ['name']}
    list_display = ['name', 'created_on', 'status']
    search_fields = ['name']
    list_filter = ['name']


class PageAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_on', 'status']
    search_fields = ['title']
    list_filter = ['title']


class TestingForm(forms.Form):
    first_name = forms.CharField(max_length=200, min_length=15)
    last_name = forms.CharField(max_length=200, min_length=15)
    roll_number = forms.IntegerField(
        help_text="Enter 6 digit roll number"
    )
    password = forms.CharField(widget=forms.PasswordInput())


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

                print('----------------YES----------------------')
            else:
                print('----------------NO----------------------')

        response = super().changelist_view(request, extra_context)
        return response


admin.site.register(Service, ServiceAdmin)
admin.site.register(ServiceOffering, ServiceOfferingAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(Menu, MenuAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(Contact)
