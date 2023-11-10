from django.contrib import admin

# Register your models here.
from courses.models import Course, Lesson, Test, Question, Answer


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'preview', 'description', 'owner')


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'preview', 'description', 'lesson_url', 'course', 'owner')


@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ('id', 'lesson', 'test_title', 'description', 'is_public', 'owner')


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'test', 'question_text')


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'answer_text', 'is_correct')
