# Курсы
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser

from courses.models import Course, Lesson, Test, Question, Answer
from courses.paginators import ListPaginator
from courses.permissions import IsOwner
from courses.serializers import LessonSerializer, CourseSerializer, TestSerializer, QuestionSerializer, \
    AnswerSerializer, TestDetailSerializer, TestListSerializer


class CourseViewSet(viewsets.ModelViewSet):
    """Отображение курсов"""
    serializer_class = CourseSerializer
    pagination_class = ListPaginator
    queryset = Course.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]


# Уроки
class LessonCreateAPIView(generics.CreateAPIView):
    """Создание урока"""
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsOwner | IsAdminUser]

    def perform_create(self, serializer):
        new_lesson = serializer.save()
        new_lesson.owner = self.request.user
        new_lesson.save()


class LessonListAPIView(generics.ListAPIView):
    """Вывод списка уроков"""
    serializer_class = LessonSerializer
    pagination_class = ListPaginator
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated]


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    """Вызов конкретного урока"""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated]


class LessonUpdateAPIView(generics.UpdateAPIView):
    """Изменение урока"""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsOwner | IsAdminUser]


class LessonDestroyAPIView(generics.DestroyAPIView):
    """Удаление урока"""
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsOwner | IsAdminUser]


class TestCreateAPIView(generics.ListCreateAPIView):
    """Создание теста"""
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    def perform_create(self, serializer):
        new_test = serializer.save()
        new_test.owner = self.request.user
        new_test.save()


class TestDetailAPIView(generics.RetrieveAPIView):
    """Информация по конкретному тесту"""
    queryset = Test.objects.all()
    serializer_class = TestDetailSerializer
    permission_classes = [IsAuthenticated, IsOwner | IsAdminUser]


class TestListAPIView(generics.ListAPIView):
    """Информация о тестах"""
    queryset = Test.objects.all()
    serializer_class = TestListSerializer
    permission_classes = [IsAuthenticated, IsOwner | IsAdminUser]


class TestUpdateAPIView(generics.UpdateAPIView):
    """Обновление теста"""
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


class TestDestroyAPIView(generics.DestroyAPIView):
    """Удаление теста"""
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


class QuestionListCreateAPIView(generics.ListCreateAPIView):
    """Создание вопросов"""
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


class AnswerListCreateAPIView(generics.ListCreateAPIView):
    """Создание ответов"""
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
