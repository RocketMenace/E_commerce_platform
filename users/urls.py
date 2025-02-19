from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from users.apps import UsersConfig
from users.views import UserCreateAPIView, UserDeleteAPIView, UserDetailAPIView

app_name = UsersConfig.name

urlpatterns = [
    path("register", UserCreateAPIView.as_view(), name="register"),
    path("delete/<int:user_id>", UserDeleteAPIView.as_view(), name="delete"),
    path("<int:user_id>", UserDetailAPIView.as_view(), name="detail"),
    # Token urls
    path(
        "login",
        TokenObtainPairView.as_view(permission_classes=[AllowAny]),
        name="login",
    ),
    path("token/refresh", TokenRefreshView.as_view(), name="token_refresh"),
]
