import pytest
from django.core.exceptions import ValidationError

from contacts.models import Contact


def test_create_contact(create_contact_for_test):
    data = {
        "email": "example@mail.com",
        "country": "RU",
        "city": "Moscow",
        "street": "test street",
        "house_number": 25,
    }
    assert create_contact_for_test.items() >= data.items()
