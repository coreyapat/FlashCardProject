from rest_framework import serializers
from .models import FlashCards, CollectionPoint


class FlashCardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlashCards
        fields = ['cardId', 'front', 'back']


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollectionPoint
        fields = ['cardId', 'name']
