from rest_framework import serializers
from .models import Menu

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['id', 'restaurant', 'date', 'items', 'votes_count']

class MenuDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['id', 'restaurant', 'date', 'items', 'votes_count']