from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Quiz
from .serializers import QuizSerializer


class QuizListView(APIView):

    permission_classes = [permissions.AllowAny]

    def get(self, request):

        try:
            quizzes_all = Quiz.objects.all()
            serializer_quizzes = QuizSerializer(quizzes_all, many=True)

        except ObjectDoesNotExist:
            raise Http404

        return Response(serializer_quizzes.data)
