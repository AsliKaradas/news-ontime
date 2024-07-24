from django.contrib import admin
from .models import Article, Author, Category, Comment
# Register your models here.

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    summernote_fields = ('news_overview', 'news_content')
    prepopulated_fields = {'slug': ('news_title',)}
    search_fields = ['news_title', 'news_content']
    list_display = ('news_title', 'created_on')


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    search_fields = ['user']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['category_name']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'content', 'news', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('user', 'content')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)