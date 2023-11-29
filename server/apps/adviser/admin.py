from django.contrib import admin

from server.apps.adviser.models import Link, Category


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url', 'owner', 'source', 'category', 'created_at', 'updated_at', 'is_active')
    search_fields = ('id', 'name', 'source')
    list_filter = ('owner', 'category', 'source', 'created_at', 'updated_at', 'is_active')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'created_at', 'updated_at', 'is_active')
    search_fields = ('id', 'type')
    list_filter = ('created_at', 'updated_at', 'is_active')