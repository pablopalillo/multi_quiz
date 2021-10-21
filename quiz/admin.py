from django.contrib import admin
from .models import Quiz


class QuizAdmin(admin.ModelAdmin):
    readonly_fields = ('id_quiz',)


admin.site.register(Quiz, QuizAdmin)
