"""beyond_aviation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve

admin.site.site_header = 'Go Above And Beyond'
admin.site.site_title = 'Go Above And Beyond Admin Site'
admin.site.index_title = 'Go Above And Beyond'

urlpatterns = [
    path('', include('website.urls')),
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
]
handler500 = 'website.views.error_500_view'
handler404 = 'website.views.error_404_view'
urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
]
