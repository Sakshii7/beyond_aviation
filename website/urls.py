from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='Homepage'),
    path('<slug:slug>', views.view_page, name='View Page'),
    path('services/<slug:slug>', views.view_service, name='View Service'),
    path('query_form/', views.query_form, name='Query Form'),
]
