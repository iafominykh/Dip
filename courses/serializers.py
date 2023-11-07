from rest_framework import serializers
from courses.models import Course, Lesson, Question, Test, Answer


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = '__all__'


class TestDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = ['id', 'test_title', 'description']


class TestListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = ['test_title']


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'
