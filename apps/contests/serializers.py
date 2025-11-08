from rest_framework import serializers
from .models import Contest


class ContestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contest
        fields = ['id', 'name', 'description', 'start_date', 'end_date', 
                  'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']


class ContestCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contest
        fields = ['name', 'description', 'start_date', 'end_date']

