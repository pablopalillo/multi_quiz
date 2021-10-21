from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Questions, Answers


class QuestionsModelTest(TestCase):

    fixtures = ["fixtures/quiz.json", "fixtures/questions.json"]

    def test_title_max_length(self):
        question = Questions()  # object from Quiz model
        max_length = question._meta.get_field('question_title').max_length
        self.assertEquals(max_length, 100)

        large_title = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam congue"

        self.assertTrue(len(large_title) <= 100)

    def test_check_display_question_model(self):
        questions = Questions.objects.first()
        # should return a str display model
        self.assertTrue(isinstance(questions.__str__(), str), "Obj have incorrect str method")

    def test_select_questions_by_quiz(self):
        """
        Test basic pass to model function select_questions_by_quiz
        :return: Questions
        """
        id_test_quiz = 1
        question_selected = Questions().select_question_by_quiz(id_test_quiz)
        self.assertTrue(isinstance(question_selected, Questions))


class AnswersModelTest(TestCase):

    fixtures = ["fixtures/quiz.json", "fixtures/questions.json"]

    def test_title_max_length(self):
        answer = Answers()  # object from Quiz model

        large_answer = "Lorem ipsum dolor sit amet, consectetur adipiscing" \
            "elit. Nullam congue Donec faucibus metus sem, quis consectetur"\
            "sapien commodo et. Ut eleifend ex et ipsum sagittis auctor."\
            "Curabitur vitae tincidunt dolor. In et erat ut dui tempus "\
            "pellentesque. Sed libero elit, vestibulum et sem ac, aliquet"\
            "vulputate velit."

        self.assertTrue(len(large_answer) <= 500)

    def test_check_display_answers_model(self):
        answer = Answers.objects.first()
        # should return a str display model
        self.assertTrue(isinstance(answer.__str__(), str), "Obj have incorrect str method")


class QuestionsListViewTest(APITestCase):

    fixtures = ["fixtures/quiz.json", "fixtures/questions.json"]

    def test_verify_accessible(self):

        url = "/questions"

        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class QuestionsViewTest(APITestCase):

    fixtures = ["fixtures/quiz.json", "fixtures/questions.json"]

    def test_verify_accessible(self):

        id_test_quiz = 1
        url = "/questions/{}".format(id_test_quiz)

        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
