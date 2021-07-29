from django.urls import path
from . import views


urlpatterns = [
    path('Flash/', views.FlashCardsList.as_view()),
    path('flashcard/<int:cardId>', views.FlashCardsList.as_view()),
]