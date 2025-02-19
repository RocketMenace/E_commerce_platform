from typing import Any

from django.contrib.auth.hashers import make_password
from django.http import Http404
from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework.generics import get_object_or_404

from users.models import User


def create_user(data: dict[str, Any]) -> User:
    user = User.objects.create(
        email=data["email"], password=make_password(data["password"])
    )
    return user


def delete_user(user_id: int):
    try:
        user = get_object_or_404(User, id=user_id)
        user.delete()
    except Http404:
        raise APIException(
            detail=f"Пользователь с {user_id=} не существует",
            code=status.HTTP_404_NOT_FOUND,
        )


def get_user(user_id: int):
    try:
        user = get_object_or_404(User, id=user_id)
        return user
    except Http404:
        raise APIException(
            detail=f"Пользователь с {user_id=} не существует",
            code=status.HTTP_404_NOT_FOUND,
        )
