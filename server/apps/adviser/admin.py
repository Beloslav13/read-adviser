from django.contrib import admin

from server.apps.adviser.models import Link, Category
from server.apps.adviser.models.rating import Rating


class RatingInline(admin.TabularInline):
    model = Rating
    fields = ['id', 'rate', 'link', 'owner', 'created_at', 'updated_at', 'is_active']
    readonly_fields = ['id', 'created_at', 'updated_at']
    extra = 1

@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    inlines = [RatingInline]

    list_display = ('id', 'name', 'url', 'owner', 'source', 'category', 'created_at', 'updated_at',
                    'is_read', 'is_active')
    search_fields = ('id', 'name', 'source')
    list_filter = ('owner', 'category', 'source', 'created_at', 'updated_at', 'is_read', 'is_active')

    # def get_rating(self, obj):
    #     return [rating.rate for rating in obj.rating.all()]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'created_at', 'updated_at', 'is_active')
    search_fields = ('id', 'type')
    list_filter = ('created_at', 'updated_at', 'is_active')


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('id', 'rate', 'link', 'owner', 'created_at', 'updated_at', 'is_active')
    search_fields = ('id', 'type')
    list_filter = ('created_at', 'updated_at', 'is_active')