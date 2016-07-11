from django.contrib import admin

from .models import Tag
from .models import Category

admin.site.register(Tag)
admin.site.register(Category)
