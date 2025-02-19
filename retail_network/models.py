from django.db import models
from django.db.models.fields import return_None
from django.utils.html import format_html
from rest_framework.reverse import reverse

from contacts.models import Contact
from products.models import Product

# Create your models here.


class NetworkNode(models.Model):
    title = models.CharField(max_length=200, verbose_name="название")
    contacts = models.OneToOneField(
        Contact,
        related_name="owner",
        verbose_name="контакты",
        on_delete=models.CASCADE,
    )
    products = models.ManyToManyField(
        Product, related_name="producer", verbose_name="продукты"
    )
    supplier = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="поставщик",
    )
    debt = models.DecimalField(
        decimal_places=2,
        max_digits=12,
        default=0.00,
        verbose_name="задолженность перед поставщиком",
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="дата создания")

    class Meta:
        db_table_comment = "Звено сети"
        db_table = "network_nodes"
        ordering = ["title"]
        indexes = [models.Index(fields=["title"])]
        verbose_name = "звено сети"
        verbose_name_plural = "звенья сети"

    def __str__(self):
        return f"{self.title}"

    def supplier_link(self):
        if self.supplier:
            url = reverse(
                "admin:retail_network_networknode_change", args=[self.supplier.id]
            )
            return format_html('<a href="{}">{}</a>', url, self.supplier.title)
        return "-"

    def get_city(self):
        return self.contacts.city
