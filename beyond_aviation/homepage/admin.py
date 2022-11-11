from django.contrib import admin

from .models import *


# Register your models here.
# class HomepageService(admin.ModelAdmin):
#     list_display = ('title')


admin.site.register(Service)
admin.site.register(ServiceOffering)
