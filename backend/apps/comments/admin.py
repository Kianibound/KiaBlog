from django.contrib import admin
from .models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['author_name', 'article', 'content', 'created_at']
    search_fields = ['author_name', 'author_email', 'content']
    list_filter = ['created_at', 'article']
    readonly_fields = ['created_at', 'updated_at']
    ordering = ['-created_at']
