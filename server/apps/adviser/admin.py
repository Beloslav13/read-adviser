from django.contrib import admin

from server.apps.adviser.models import Link, Category


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url', 'owner', 'category', 'created_at', 'updated_at')
    search_fields = ('id', 'name')
    list_filter = ('owner', 'category', 'created_at', 'updated_at')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'created_at', 'updated_at')
    search_fields = ('id', 'type')
    list_filter = ('created_at', 'updated_at')