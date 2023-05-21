from django.contrib import admin
from .models import Course,Lesson,LessonCompleted, Question, QuestionChoice
# Register your models here.


class LessonAdmin(admin.ModelAdmin):
        list_display = ["title", "course", "lessonNumber", "onlyForAdmin"]

class QuestionChoiceAdmin(admin.ModelAdmin):
        list_display = ["question", "answer", "is_correct"]

class QuestionAdmin(admin.ModelAdmin):
        list_display = ["question", "type"]

class LessonCompletedAdmin(admin.ModelAdmin):
        list_display = ["lesson", "user"]


admin.site.register(Course)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(LessonCompleted, LessonCompletedAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(QuestionChoice, QuestionChoiceAdmin)
