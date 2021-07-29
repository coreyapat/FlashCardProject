from rest_framework import serializers
from .models import FlashCards


class FlashCardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlashCards
        fields = ['id', 'front', 'back']


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollectionPoint
        fields = ['id', 'name']
