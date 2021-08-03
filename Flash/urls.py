from django.urls import path
from . import views


urlpatterns = [
    path('Flash/', views.FlashCardsList.as_view()),
    path('flashcard/<int:card>/', views.FlashCardsList.as_view()),
    path('flashcard/', views.CreateCard.as_view()),
    path('flashcard/<int:fk>/', views.FlashCardInfo.as_view()),
]