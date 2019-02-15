from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('ajax_handler/', views.ajax_handler, name='ajax_handler'),
]