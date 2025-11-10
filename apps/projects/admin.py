from django.contrib import admin
from .models import Project, ProjectMedia


class ProjectMediaInline(admin.TabularInline):
    model = ProjectMedia
    extra = 1
    fields = ('media',)
    readonly_fields = ('created_at', 'updated_at')


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    search_fields = ('name', 'description')
    list_filter = ('created_at',)
    ordering = ('-created_at',)
    inlines = (ProjectMediaInline,)
    readonly_fields = ('created_at', 'updated_at')


@admin.register(ProjectMedia)
class ProjectMediaAdmin(admin.ModelAdmin):
    list_display = ('project', 'media', 'created_at', 'updated_at')
    search_fields = ('project__name',)
    raw_id_fields = ('project',)
    readonly_fields = ('created_at', 'updated_at')
