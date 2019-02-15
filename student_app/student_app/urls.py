from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('ajax_handler/', include('main.urls')),
    path('', include('main.urls')),
]
