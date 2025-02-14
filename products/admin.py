from django.contrib import admin

from products.models import Product


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "model", "release_date"]
    list_filter = ["name", "model", "release_date"]
    search_fields = ["name", "model", "release_date"]
    ordering = ["release_date", "name"]
