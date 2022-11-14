from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='Homepage'),
    path('view_service/<int:service_id>', views.view_service, name='View Service'),
]