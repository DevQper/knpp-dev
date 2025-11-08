from rest_framework import serializers
from .models import Project, ProjectMedia


class ProjectMediaSerializer(serializers.ModelSerializer):
    media = serializers.FileField(use_url=True)
    
    class Meta:
        model = ProjectMedia
        fields = ['id', 'project', 'media', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']


class ProjectSerializer(serializers.ModelSerializer):
    media = ProjectMediaSerializer(many=True, read_only=True)
    
    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'created_at', 'updated_at', 'media']
        read_only_fields = ['created_at', 'updated_at']


class ProjectCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['name', 'description']

