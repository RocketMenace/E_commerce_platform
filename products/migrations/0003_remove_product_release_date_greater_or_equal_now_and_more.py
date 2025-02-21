# Generated by Django 4.2 on 2025-02-20 09:58

import datetime

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0002_remove_product_release_date_greater_or_equal_now_and_more"),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name="product",
            name="release_date_greater_or_equal_now",
        ),
        migrations.AddConstraint(
            model_name="product",
            constraint=models.CheckConstraint(
                check=models.Q(
                    (
                        "release_date__gt",
                        datetime.datetime(2025, 2, 20, 9, 58, 26, 979918),
                    )
                ),
                name="release_date_greater_or_equal_now",
            ),
        ),
    ]
