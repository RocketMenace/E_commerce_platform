from django.contrib import admin

from retail_network.models import NetworkNode

# Register your models here.


@admin.register(NetworkNode)
class NetworkNode(admin.ModelAdmin):
    list_display = ["title", "supplier", "debt", "created_at"]
    list_filter = ["title", "supplier"]
    search_fields = ["title", "supplier"]
    ordering = ["-created_at", "title"]
