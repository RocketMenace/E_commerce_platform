from django.urls import path

from contacts.apps import ContactsConfig
from contacts.views import ContactCreateAPIView, ContactDeleteAPIView, ContactDetailAPIView, ContactUpdateAPIView

app_name = ContactsConfig.name

urlpatterns = [
    path("create", ContactCreateAPIView.as_view(), name="create"),
    path("delete/<int:contact_id>", ContactDeleteAPIView.as_view(), name="delete"),
    path("<int:contact_id>", ContactDetailAPIView.as_view(), name="detail"),
    path("update/<int:contact_id", ContactUpdateAPIView.as_view(), name="update")
]
