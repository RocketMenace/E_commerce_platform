# Generated by Django 4.2 on 2025-02-15 08:26

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=200, verbose_name="название продукта"),
                ),
                (
                    "model",
                    models.CharField(
                        max_length=200, unique=True, verbose_name="название модели"
                    ),
                ),
                ("release_date", models.DateTimeField()),
            ],
            options={
                "verbose_name": "продукт",
                "verbose_name_plural": "продукты",
                "db_table": "products",
                "db_table_comment": "Продукты сети",
                "ordering": ["release_date"],
            },
        ),
        migrations.AddIndex(
            model_name="product",
            index=models.Index(
                fields=["name", "model"], name="products_name_51fdb9_idx"
            ),
        ),
    ]
