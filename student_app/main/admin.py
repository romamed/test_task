from django.contrib import admin

from .models import Person
from .models import Document

admin.site.register(Person)
admin.site.register(Document)