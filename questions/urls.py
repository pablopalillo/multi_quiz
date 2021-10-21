from django.urls import path, include

from . import views


urlpatterns = [
   path('questions', views.QuestionsListView.as_view()),
   path('question/<int:id_question>', views.QuestionView.as_view()),
   path('questions/<int:id_quiz>', views.QuestionsQuizView.as_view()),
]
