from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig
from users.views import UserDestroyAPIView, UserUpdateAPIView, UserCreateAPIView, UserListAPIView

app_name = UsersConfig.name

urlpatterns = [
    # Пользователи
    path('', UserListAPIView.as_view(), name='list_user'),
    path('create/', UserCreateAPIView.as_view(), name='create_user'),
    path('update/<int:pk>/', UserUpdateAPIView.as_view(), name='update_user'),
    path('delete/<int:pk>/', UserDestroyAPIView.as_view(), name='delete_user'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]