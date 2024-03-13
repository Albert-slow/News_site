from django.contrib import admin

from .models import CategoryModel, TagModel, ArticleModel


@admin.register(CategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_title', 'created_at']
    search_fields = ['category_title']
    list_filter = ['created_at']


@admin.register(TagModel)
class TagAdmin(admin.ModelAdmin):
    list_display = ['tag_title']


@admin.register(ArticleModel)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['article_title', 'article_author', 'article_created_at']
    search_fields = ['article_title', 'article_author']
    list_filter = ['article_created_at', 'article_author']


