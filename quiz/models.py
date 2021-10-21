from django.db import models


class Quiz(models.Model):
    id_quiz = models.AutoField(primary_key=True)
    quiz_name = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.quiz_name
