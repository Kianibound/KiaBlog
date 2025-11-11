from django.contrib import admin

from apps.articles.models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'created_at', 'updated_at']
    search_fields = ['title', 'content']
    readonly_fields = ['created_at', 'updated_at', 'slug']
    list_filter = ['created_at']
    ordering = ['-created_at']

# admin.site.register(Article)
