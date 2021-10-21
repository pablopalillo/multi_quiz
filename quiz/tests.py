from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Quiz


class QuizModelTest(TestCase):

    fixtures = ["fixtures/quiz.json"]

    def test_title_max_length(self):
        quiz = Quiz()  # object from Quiz model
        max_length = quiz._meta.get_field('quiz_name').max_length
        self.assertEquals(max_length, 150)

        large_title = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam congue",\
            "risus nec sodales mollis. Fusce tempor quam eget ante fringilla tempus. "

        self.assertTrue(len(large_title) <= 150)

    def test_check_display_model(self):
        quiz = Quiz.objects.first()
        # should return a str display model
        self.assertTrue(isinstance(quiz.__str__(), str), "Obj have incorrect str method")


class QuizListViewTest(APITestCase):

    fixtures = ["fixtures/quiz.json"]

    def test_verify_accessible(self):

        url = "/quizzes"

        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
