from rest_framework import serializers
from .models import Proposal


class ProposalSerializer(serializers.ModelSerializer):
    file = serializers.FileField(use_url=True)
    
    class Meta:
        model = Proposal
        fields = ['id', 'proposed_by', 'phone_number', 'email', 'file', 'title', 
                  'description', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']


class ProposalCreateUpdateSerializer(serializers.ModelSerializer):
    file = serializers.FileField(use_url=True)
    
    class Meta:
        model = Proposal
        fields = ['proposed_by', 'phone_number', 'email', 'file', 'title', 'description']

