from django.contrib import admin

from contacts.models import Contact

# Register your models here.


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ["email", "country", "city", "street", "house_number"]
    list_filter = ["country", "city"]
    search_fields = ["email", "country", "city"]
    ordering = ["email"]
