from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='homepage'),
    path('services/<slug:slug>', views.view_service, name='view_service'),
    path('<slug:slug>', views.view_pages, name='view_pages'),
    path('query_form/', views.query_form, name='Query Form'),
]
