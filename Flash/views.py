from django.http import Http404
from django.shortcuts import render
from .models import FlashCards, CollectionPoint
from .serializers import FlashCardsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
class FlashCardsList(APIView):

    def get(self, FlashCards):
        flashcards = FlashCards.objects.all()
        serializer = FlashCardsSerializer(flashcards, many=True)
        return Response(serializer.data)


    def post(self, request):
        serializer = FlashCardsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FlashIdList(APIView):

    def filter_by_id(self, cardId):
        try:
            return FlashCards.objects.filter(cardId=cardId)
        except cardId.DoesNotExist:
            raise Http404

    def get(self, request, cardId):
        card_id = self.filter_by_id(cardId)
        serializer = FlashCardsSerializer(card_id, many=True)
        return Response(serializer.data)
