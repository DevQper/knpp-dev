from django.contrib import admin
from .models import News, NewsMedia


class NewsMediaInline(admin.TabularInline):
    model = NewsMedia
    extra = 1
    fields = ('media',)
    readonly_fields = ('created_at', 'updated_at')


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ('title', 'description')
    list_filter = ('created_at',)
    ordering = ('-created_at',)
    inlines = (NewsMediaInline,)
    readonly_fields = ('created_at', 'updated_at')


@admin.register(NewsMedia)
class NewsMediaAdmin(admin.ModelAdmin):
    list_display = ('news', 'media', 'created_at', 'updated_at')
    search_fields = ('news__title',)
    raw_id_fields = ('news',)
    readonly_fields = ('created_at', 'updated_at')
