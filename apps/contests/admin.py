from django.contrib import admin
from .models import Contest


@admin.register(Contest)
class ContestAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date', 'created_at', 'updated_at')
    search_fields = ('name', 'description')
    list_filter = ('start_date', 'end_date', 'created_at')
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')
