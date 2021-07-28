from rest_framework import serializers
from .models import FlashCards


class FlashCardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlashCards
        fields = ['id', 'front', 'back']