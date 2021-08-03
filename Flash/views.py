from django.http import Http404
from django.shortcuts import render
from .models import CollectionPoint, FlashCards
from .serializers import FlashCardsSerializer, CollectionSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
class FlashCardsList(APIView):

    def get(self, request):
        flashcards = CollectionPoint.objects.all()
        serializer = CollectionSerializer(flashcards, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FlashCardsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FlashIdList(APIView):

    def filter_by_id(self, card):
        try:
            return FlashCards.objects.filter(card=card)
        except card.DoesNotExist:
            raise Http404

    def get(self, request, card):
        card_id = self.filter_by_id(card)
        serializer = CollectionSerializer(card_id, many=True)
        return Response(serializer.data)


class CreateCard(APIView):

    def post(self, request):
        serializer = FlashCardsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FlashCardInfo(APIView):

    def get_by_id(self, fk):
        try:
            return FlashCards.objects.get(fk=fk)
        except FlashCards.DoesNotExist:
            raise Http404

    def put(self, request, fk):
        flashCard_Id = self.get_by_id(fk)
        updatedFlashCard = FlashCardsSerializer(flashCard_Id, data=request.data, partial=True)
        if updatedFlashCard.is_valid():
            updatedFlashCard.save()
            return Response(updatedFlashCard.data, status=status.HTTP_202_ACCEPTED)
        return Response(updatedFlashCard.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

    def delete(self, request, fk):
        flashCard_Id = self.get_by_id(fk)
        deleteFlashCard = FlashCardsSerializer(flashCard_Id)
        flashCard_Id.delete()
        return Response(deleteFlashCard.data, status=status.HTTP_200_OK)
