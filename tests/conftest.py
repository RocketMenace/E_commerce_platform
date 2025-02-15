from datetime import datetime
from typing import Any

import pytest
from rest_framework.test import APIClient

from contacts.models import Contact
from products.models import Product


@pytest.fixture(scope="function")
def api_client() -> APIClient:
    yield APIClient()


@pytest.fixture()
def create_contact_for_test() -> dict[str, Any]:
    data = {
        "email": "example@mail.com",
        "country": "RU",
        "city": "Moscow",
        "street": "test street",
        "house_number": 25,
    }
    return data


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


@pytest.fixture()
def create_product_for_test() -> Product:
    data = {
        "name": "Test product",
        "model": "Test model",
        "release_date": datetime.now(),
    }
    return Product(**data)
