from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='Homepage'),
    path('<slug:slug>', views.view_service, name='view_service'),
    path('<slug:slug_about>/', views.view_menu, name='view_menu'),
]