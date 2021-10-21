from rest_framework import serializers
from .models import Questions, Answers


class AnswersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answers
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):

    answers = AnswersSerializer(many=True, read_only=True)

    class Meta:
        model = Questions
        fields = ['id_question', 'question_title', 'answers']


class QuestionQuizSerializer(serializers.ModelSerializer):

    answers = AnswersSerializer(many=True, read_only=True)

    class Meta:
        model = Questions
        fields = ['id_question', 'quiz', 'question_title', 'answers']
