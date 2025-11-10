from django.contrib import admin
from .models import Proposal


@admin.register(Proposal)
class ProposalAdmin(admin.ModelAdmin):
    list_display = ('title', 'proposed_by', 'email', 'phone_number', 'created_at', 'updated_at')
    search_fields = ('title', 'proposed_by', 'email', 'phone_number')
    list_filter = ('created_at',)
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')
