from django.shortcuts import render
from .models import FlashCards
from .serializers import FlashCardsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
class FlashCardsList(APIView):

    def get(self, request):
        flashcards = FlashCards.objects.all()
        serializer = FlashCardsSerializer(flashcards, many=True)
        return Response(serializer.data)


    def post(self, request):
        serializer = FlashCardsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)