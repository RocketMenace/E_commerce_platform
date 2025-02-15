from typing import Any

from django.http import Http404
from rest_framework.generics import get_object_or_404
from rest_framework.exceptions import APIException
from rest_framework import status

from contacts.models import Contact


def create_contact(data: dict[str, Any]) -> Contact:
    contact = Contact.objects.create(**data)
    return contact

def delete_contact(contact_id: int):
    try:
        contact = get_object_or_404(Contact, id=contact_id)
        contact.delete()
    except Http404:
        raise APIException(detail=f"Контакт с {contact_id=} не существует", code=status.HTTP_404_NOT_FOUND)

def get_contact(contact_id: int):
    try:
        return get_object_or_404(Contact, id=contact_id)
    except Http404:
        raise APIException(detail=f"Контакт с {contact_id=} не существует", code=status.HTTP_404_NOT_FOUND)

def update_contact(contact_id:int, data: dict[str, Any]):
    try:
        contact = get_object_or_404(Contact, id=contact_id)
        contact.__dict__.update(**data)
        contact.save()
    except Http404:
        raise APIException(detail=f"Контакт с {contact_id=} не существует", code=status.HTTP_404_NOT_FOUND)

