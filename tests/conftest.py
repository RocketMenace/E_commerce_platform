from typing import Any

import pytest

from contacts.models import Contact


@pytest.fixture()
def create_contact_for_test() -> Contact:
    data = {
        "email": "example@mail.com",
        "country": "Russia",
        "city": "Moscow",
        "street": "test street",
        "house_number": 25,
    }
    return Contact(**data)


@pytest.fixture()
def create_contact_for_test_with_invalid_country() -> Contact:
    data = {
        "email": "example@mail.com",
        "country": "Something wrong",
        "city": "Moscow",
        "street": "test street",
        "house_number": 25,
    }
    return Contact(**data)
