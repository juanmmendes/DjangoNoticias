from django.contrib import admin
from .models import NewsArticle

@admin.register(NewsArticle)
class NewsArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'source', 'published_at', 'created_at']
    list_filter = ['source', 'published_at']
    search_fields = ['title', 'description']
    readonly_fields = ['created_at']
