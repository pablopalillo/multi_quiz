from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Questions
from .serializers import QuestionSerializer, QuestionQuizSerializer


class QuestionsListView(APIView):

    permission_classes = [permissions.AllowAny]

    def get(self, request):

        try:
            question_all = Questions.objects.prefetch_related("answers")
            serializer_question = QuestionSerializer(question_all, many=True)

        except ObjectDoesNotExist:
            raise Http404

        return Response(serializer_question.data)


class QuestionView(APIView):

    permission_classes = [permissions.AllowAny]

    def get(self, request, id_question):

        try:
            question = Questions.objects.select_question_by_id(id_question)
            serializer_question = QuestionSerializer(question)

        except ObjectDoesNotExist:
            raise Http404

        return Response(serializer_question.data)


class QuestionsQuizView(APIView):

    permission_classes = [permissions.AllowAny]

    def get(self, request, id_quiz):

        try:
            questions = Questions.objects_answers.filter(quiz__id_quiz=id_quiz)
            serializer_question = QuestionQuizSerializer(questions, many=True)

        except ObjectDoesNotExist:
            raise Http404

        return Response(serializer_question.data)
