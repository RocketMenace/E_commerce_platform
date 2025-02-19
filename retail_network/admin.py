from django.contrib import admin
from django.contrib import messages
from django.utils.translation import ngettext

from retail_network.models import NetworkNode

# Register your models here.




@admin.register(NetworkNode)
class NetworkNode(admin.ModelAdmin):
    list_display = ["title", "supplier_link", "debt", "created_at", "get_city"]
    list_filter = ["title", "supplier","contacts__city"]
    search_fields = ["title", "supplier"]
    ordering = ["-created_at", "title"]
    actions = ["debt_set_default"]

    @admin.action(description="Сбросить задолженность перед поставщиком")
    def debt_set_default(self, request, queryset):
        updated = queryset.update(debt=0.00)
        self.message_user(
            request,
            ngettext("%d задолженность перед поставщиком успешно погашена",
                     "%d задолженности перед поставщиками успешно погашены",
                     updated,
                     )
            % updated,
            messages.SUCCESS
        )

    def supplier_link(self, obj):
        return obj.supplier_link()

    def get_city(self, obj):
        return obj.get_city()

    supplier_link.short_description = "Поставщик"
    get_city.short_description = "Город"