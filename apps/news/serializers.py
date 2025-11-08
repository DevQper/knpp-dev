from rest_framework import serializers
from .models import News, NewsMedia


class NewsMediaSerializer(serializers.ModelSerializer):
    media = serializers.FileField(use_url=True)
    
    class Meta:
        model = NewsMedia
        fields = ['id', 'news', 'media', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']


class NewsSerializer(serializers.ModelSerializer):
    media = NewsMediaSerializer(many=True, read_only=True)
    
    class Meta:
        model = News
        fields = ['id', 'title', 'description', 'created_at', 'updated_at', 'media']
        read_only_fields = ['created_at', 'updated_at']


class NewsCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['title', 'description']

