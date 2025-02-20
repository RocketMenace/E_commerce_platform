from datetime import datetime, timedelta, timezone
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
def create_contact_for_test_in_api(api_client, login_user_for_tests):
    payload = {
        "email": "example_1@mail.com",
        "country": "RU",
        "city": "Moscow",
        "street": "test street",
        "house_number": 25,
    }
    response = api_client.post(
        "/contacts/create",
        data=payload,
        format="json",
        headers={"Authorization": "Bearer " + login_user_for_tests},
    )
    return response.data


@pytest.fixture()
def create_retail_network_for_tests(
    api_client, create_contact_for_test_in_api, login_user_for_tests
):
    date = datetime.now(tz=timezone.utc) + timedelta(days=1)
    payload = {
        "title": "Test network_777",
        "contacts": create_contact_for_test_in_api["id"],
        "products": [
            {
                "name": "Test product",
                "model": "Test model",
                "release_date": date.isoformat(),
            }
        ],
    }
    response = api_client.post(
        "/retail_network/create",
        data=payload,
        format="json",
        headers={"Authorization": "Bearer " + login_user_for_tests},
    )
    return response.data


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
def create_product_for_test() -> dict[str, Any]:
    data = {
        "name": "Test product",
        "model": "Test model",
        "release_date": datetime.now().isoformat() + "Z",
    }
    return data


@pytest.fixture()
def create_user_for_tests(api_client):
    payload = {"email": "test_777@example.com", "password": "qwerasdf123"}
    response = api_client.post("/users/register", data=payload, format="json")
    return response.data


@pytest.fixture()
def login_user_for_tests(api_client, create_user_for_tests):
    payload = {"email": "test_777@example.com", "password": "qwerasdf123"}
    response = api_client.post("/users/login", data=payload, format="json")
    return response.data["access"]
