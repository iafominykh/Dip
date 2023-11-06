from rest_framework import serializers
from courses.models import Course, Lesson


MANYABLE = {'many': True, 'read_only': True}


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):


    class Meta:
        model = Course
        fields = '__all__'