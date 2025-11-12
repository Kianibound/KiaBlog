from django.contrib import admin

from apps.categories_tags.models import Category, Tag


admin.site.register(Category)
admin.site.register(Tag)
