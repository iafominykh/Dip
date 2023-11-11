
from rest_framework import viewsets, generics


from users.models import User
from users.serializers import UserSerializer


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    """Отображение пользователей"""
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserCreateAPIView(generics.CreateAPIView):
    """Создание пользователей"""
    serializer_class = UserSerializer


class UserListAPIView(generics.ListAPIView):
    """Отображение пользователей"""
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserUpdateAPIView(generics.UpdateAPIView):
    """Обновление пользователей"""
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserDestroyAPIView(generics.DestroyAPIView):
    """Удаление пользователей"""
    queryset = User.objects.all()