from django.urls import path

from courses.apps import CoursesConfig
from rest_framework.routers import DefaultRouter

from courses.views import CourseViewSet, LessonCreateAPIView, LessonListAPIView, LessonRetrieveAPIView, \
    LessonUpdateAPIView, LessonDestroyAPIView, TestCreateAPIView, TestDetailAPIView, \
    TestUpdateAPIView, TestDestroyAPIView, QuestionListCreateAPIView, TestListAPIView, \
    AnswerListCreateAPIView
from users.apps import UsersConfig

app_name = UsersConfig.name

router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='courses')

urlpatterns = [
                  # Уроки
                  path('lesson/create/', LessonCreateAPIView.as_view(), name='create_lesson'),
                  path('lesson/', LessonListAPIView.as_view(), name='list_lesson'),
                  path('lesson/<int:pk>/', LessonRetrieveAPIView.as_view(), name='get_lesson'),
                  path('lesson/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='update_lesson'),
                  path('lesson/delete/<int:pk>/', LessonDestroyAPIView.as_view(), name='delete_lesson'),
                  path('tests/create/', TestCreateAPIView.as_view(), name='test_create'),
                  path('tests/', TestListAPIView.as_view(), name='test_list'),
                  path('tests/<int:pk>/', TestDetailAPIView.as_view(), name='test_detail'),
                  path('tests/update/<int:pk>/', TestUpdateAPIView.as_view(), name='test_update'),
                  path('tests/delete/<int:pk>/', TestDestroyAPIView.as_view(), name='test_delete'),
                  path('questions/', QuestionListCreateAPIView.as_view(), name='question_create'),
                  path('answers/', AnswerListCreateAPIView.as_view(), name='answer_create'),

              ] + router.urls
