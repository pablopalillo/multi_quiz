from django.urls import path, include

from . import views


urlpatterns = [
   path('quizzes', views.QuizListView.as_view()),
]
