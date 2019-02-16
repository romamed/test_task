from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('search/', views.search, name='search'),
    path('ajax_handler/', views.ajax_handler, name='ajax_handler'),
]