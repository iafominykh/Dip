from rest_framework import serializers
from courses.models import Course, Lesson, Question, Test, Answer


class LessonSerializer(serializers.ModelSerializer):
    # Сериализатор для модели урока
    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    # Сериализатор для модели курса
    class Meta:
        model = Course
        fields = '__all__'


class TestSerializer(serializers.ModelSerializer):
    # Сериализатор для модели теста
    class Meta:
        model = Test
        fields = '__all__'


class TestDetailSerializer(serializers.ModelSerializer):
    # Сериализатор для детальной информации о тесте
    class Meta:
        model = Test
        fields = ['id', 'test_title', 'description']


class TestListSerializer(serializers.ModelSerializer):
    # Сериализатор для списка тестов
    class Meta:
        model = Test
        fields = ['test_title']


class QuestionSerializer(serializers.ModelSerializer):
    # Сериализатор для модели вопроса
    class Meta:
        model = Question
        fields = '__all__'


class AnswerSerializer(serializers.ModelSerializer):
    # Сериализатор для модели ответа
    class Meta:
        model = Answer
        fields = '__all__'
