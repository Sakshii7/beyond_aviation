from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='Homepage'),
    path('<slug:slug>', views.view_service, name='view_service'),
]