from django import forms
from django.contrib import admin
from django.db import models
from django.shortcuts import redirect
from rangefilter.filters import DateRangeFilter
from tinymce.widgets import TinyMCE

from beyond_aviation.settings import MEDIA_URL
from .models import SubSection, ServiceOffering, Service, Section, Menu, Page, QueryForm, Setting, Slider, Slides


class SubSectionAdmin(admin.TabularInline):
    model = SubSection
    fields = ['status', 'content', 'icon', 'icon_preview']
    readonly_fields = ['icon_preview']
    list_editable = ['status']


class SectionAdmin(admin.ModelAdmin):
    fields = ['status', 'title', 'section_type', 'page', 'text_align', 'description', 'image', 'image_preview',
              'show_mail_us_button', 'background_color', 'text_color']
    readonly_fields = ['image_preview']
    inlines = [SubSectionAdmin]
    list_display = ['title', 'created_on', 'status']
    list_filter = (('created_on', DateRangeFilter), 'status')
    list_editable = ['status']
    list_per_page = 10
    search_fields = ['title']
    ordering = ['-created_on']


class ServiceAdmin(admin.ModelAdmin):
    fields = ['status', 'name', 'slug', 'excerpt', 'description', 'is_featured', 'image', 'image_preview']
    readonly_fields = ['image_preview']
    # prepopulating slug from title
    prepopulated_fields = {'slug': ['name']}
    list_display = ['name', 'created_on', 'status']
    list_filter = (('created_on', DateRangeFilter), 'status')
    list_editable = ['status']
    list_per_page = 10
    search_fields = ['name']
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }
    ordering = ['-created_on']


class ServiceOfferingAdmin(admin.ModelAdmin):
    fields = ['status', 'title', 'description', 'text_align', 'icon', 'icon_preview']
    readonly_fields = ['icon_preview']
    list_display = ['title', 'created_on', 'status', ]
    list_filter = (('created_on', DateRangeFilter), 'status')
    list_editable = ['status']
    list_per_page = 10
    search_fields = ['title']
    ordering = ['-created_on']


class MenuAdmin(admin.ModelAdmin):
    fields = ['status', 'name', 'slug', 'sequence', 'show_in_footer']
    prepopulated_fields = {'slug': ['name']}
    list_display = ['name', 'created_on', 'status']
    list_filter = (('created_on', DateRangeFilter), 'status')
    list_editable = ['status']
    list_per_page = 10
    search_fields = ['name']
    ordering = ['-created_on']


class QueryFormAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'created_on']
    list_filter = (('created_on', DateRangeFilter), 'first_name')
    search_fields = ['first_name']
    ordering = ['-created_on']

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None) -> bool:
        return False


class PageModelForm(forms.ModelForm):
    meta_description = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Page
        fields = '__all__'


class PageAdmin(admin.ModelAdmin):
    fields = ['status', 'title', 'slug', 'header_img', 'header_image_preview', 'content', 'meta_title',
              'meta_description', 'meta_keywords', 'meta_img']
    prepopulated_fields = {'slug': ['title']}
    readonly_fields = ['header_image_preview']
    list_display = ['title', 'created_on', 'status']
    list_editable = ['status']
    list_filter = (('created_on', DateRangeFilter), 'status')
    list_per_page = 10
    search_fields = ['title']
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }
    ordering = ['-created_on']
    form = PageModelForm


class SettingAdmin(admin.ModelAdmin):
    change_list_template = 'admin/setting.html'

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
            common_service_content = request.POST['common_service_content']
            google_tag_manager_key = request.POST['google_tag_manager_key']

            rows_count = Setting.objects.all().count()
            if rows_count != 0:
                settings = Setting.objects.get()
                settings.contact_address = contact_address
                settings.facebook_url = facebook_url
                settings.instagram_url = instagram_url
                settings.twitter_url = twitter_url
                settings.common_service_content = common_service_content
                settings.google_tag_manager_key = google_tag_manager_key
                settings.homepage_logo = request.FILES.get(
                    'homepage_logo') if 'homepage_logo' in request.FILES else settings.homepage_logo
                settings.footer_logo = request.FILES.get(
                    'footer_logo') if 'footer_logo' in request.FILES else settings.footer_logo
                settings.fav_icon = request.FILES.get(
                    'fav_icon') if 'fav_icon' in request.FILES else settings.fav_icon
                settings.save()
            else:
                homepage_logo = request.FILES['homepage_logo']
                footer_logo = request.FILES['footer_logo']
                fav_icon = request.FILES['fav_icon']
                query_id = Setting(contact_address=contact_address, facebook_url=facebook_url,
                                   instagram_url=instagram_url, twitter_url=twitter_url,
                                   common_service_content=common_service_content,
                                   google_tag_manager_key=google_tag_manager_key, homepage_logo=homepage_logo,
                                   footer_logo=footer_logo, fav_icon=fav_icon)
                query_id.save()

            return redirect('/admin/website/setting/')

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


class SlidesAdmin(admin.TabularInline):
    model = Slides
    fields = ['status', 'slide_name', 'slide_image', 'slide_image_preview', 'text_align', 'desc_1', 'desc_2', 'desc_3']
    readonly_fields = ['slide_image_preview']
    list_editable = ['status']


class SliderAdmin(admin.ModelAdmin):
    fields = ['status', 'name', 'code']
    inlines = [SlidesAdmin]
    list_display = ['name', 'created_on', 'status']
    list_filter = (('created_on', DateRangeFilter), 'status')
    list_editable = ['status']
    search_fields = ['name']
    ordering = ['-created_on']

    def has_add_permission(self, request, obj=None):
        rows_count = Slider.objects.all().count()

        if rows_count > 0:
            return False
        return True


admin.site.register(Service, ServiceAdmin)
admin.site.register(ServiceOffering, ServiceOfferingAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(Menu, MenuAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(QueryForm, QueryFormAdmin)
admin.site.register(Setting, SettingAdmin)
admin.site.register(Slider, SliderAdmin)
