import pytest
from rest_framework import status


@pytest.mark.django_db
def test_register_user(api_client):
    payload = {"email": "testuser@example.com", "password": "qwerasdf1234"}
    response = api_client.post("/users/register", data=payload, format="json")
    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db
def test_delete_user(api_client, create_user_for_tests):
    response = api_client.delete(f"/users/delete/{create_user_for_tests['id']}")
    assert response.status_code == status.HTTP_204_NO_CONTENT


@pytest.mark.django_db
def test_get_user(api_client, create_user_for_tests):
    response = api_client.get(f"/users/{create_user_for_tests['id']}")
    assert response.status_code == status.HTTP_200_OK
    assert response.data == create_user_for_tests
