from django.contrib import admin
from .models import Answers, Questions


class AnswersAdmin(admin.ModelAdmin):
    readonly_fields = ('id_answer',)


admin.site.register(Answers, AnswersAdmin)
admin.site.register(Questions)
