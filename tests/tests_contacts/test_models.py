import pytest
from django.core.exceptions import ValidationError

from contacts.models import Contact


def test_create_contact(create_contact_for_test):
    data = {
        "email": "example@mail.com",
        "country": "Russia",
        "city": "Moscow",
        "street": "test street",
        "house_number": 25,
    }
    assert create_contact_for_test.__dict__.items() >= data.items()


# def test_create_contact_with_invalid_email(create_contact_for_test_with_invalid_country):
#
#     with pytest.raises(ValidationError) as error:
