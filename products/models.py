from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name="название продукта")
    model = models.CharField(
        max_length=200, verbose_name="название модели", unique=True
    )
    release_date = models.DateTimeField()

    class Meta:
        db_table_comment = "Продукты сети"
        db_table = "products"
        ordering = ["release_date"]
        indexes = [models.Index(fields=["name", "model"])]
        verbose_name = "продукт"
        verbose_name_plural = "продукты"

    def __str__(self):
        return f"{self.name} {self.model} {self.release_date:%d-%m-%Y}"
