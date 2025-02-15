from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="эл.почта")
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    password = models.CharField(max_length=100, verbose_name="пароль")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        db_table_comment = "Пользователи"
        db_table = "users"
        ordering = ["email"]
        indexes = [models.Index(fields=["email"])]
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"
