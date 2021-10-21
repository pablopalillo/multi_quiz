from django.db import models
from quiz.models import Quiz


class QuestionsManager(models.Manager):

    def select_question_by_id(self, id_question: int):
        """
        Optimal version of Select by ID related with answers
        :param id_question: int
        :return: Questions
        """
        return self.prefetch_related("answers") \
            .filter(id_question=id_question)\
            .first()


class QuestionAnswersManager(models.Manager):
    """
    Optimal version of queryset with related answers
    """
    def get_query_set(self):

        return super(QuestionAnswersManager, self).get_query_set()\
            .select_related("quiz") \
            .prefetch_related("answers")


class Questions(models.Model):
    id_question = models.AutoField(primary_key=True)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question_title = models.CharField(max_length=100)
    objects = QuestionsManager()
    objects_answers = QuestionAnswersManager()

    def __str__(self):
        return self.question_title


class Answers(models.Model):
    id_answer = models.AutoField(primary_key=True)
    question = models.ForeignKey(
        Questions,
        on_delete=models.CASCADE,
        related_name='answers'
    )
    answer = models.TextField()
    points = models.SmallIntegerField(default=0)

    def __str__(self):
        return str(self.id_answer)
