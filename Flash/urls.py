from django.urls import path
from . import views


urlpatterns = [
    path('Flash/', views.FlashCardsList.as_view()),
]