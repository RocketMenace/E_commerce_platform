from django.db import models
from django_countries.fields import CountryField

# Create your models here.


class Contact(models.Model):
    email = models.EmailField(max_length=200, verbose_name="эл.почта", unique=True)
    country = CountryField(verbose_name="страна")
    city = models.CharField(max_length=200, verbose_name="город")
    street = models.CharField(max_length=200, verbose_name="улица")
    house_number = models.IntegerField(verbose_name="номер дома")

    class Meta:
        db_table_comment = "Контакты сети"
        db_table = "contacts"
        ordering = ["email"]
        indexes = [models.Index(fields=["city", "email", "country"])]
        verbose_name = "контакт"
        verbose_name_plural = "контакты"

    def __str__(self):
        return self.email
