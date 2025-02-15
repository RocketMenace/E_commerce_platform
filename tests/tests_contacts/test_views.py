import pytest
from rest_framework import status


@pytest.mark.django_db
def test_create_contact(api_client, create_contact_for_test):
    payload = {**create_contact_for_test}
    response = api_client.post("/contacts/create", data=payload, format="json")
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data.items() >= payload.items()

@pytest.mark.django_db
def test_get_contact(api_client, create_contact_for_test):
    payload = {**create_contact_for_test}
    response = api_client.post("/contacts/create", data=payload, format="json")
    contact_id = response.data["id"]
    get_response = api_client.get(f"/contacts/{contact_id}")
    assert get_response.status_code == status.HTTP_200_OK

@pytest.mark.django_db
def test_delete_contact(api_client, create_contact_for_test):
    payload = {**create_contact_for_test}
    response = api_client.post("/contacts/create", data=payload, format="json")
    contact_id = response.data["id"]
    delete_response = api_client.delete(f"/contacts/delete/{contact_id}")
    assert delete_response.status_code == status.HTTP_204_NO_CONTENT

@pytest.mark.django_db
def test_update_contact(api_client, create_contact_for_test):
    payload = {**create_contact_for_test}
    response = api_client.post("/contacts/create", data=payload, format="json")
    contact_id = response.data["id"]
    response.data["city"] = "Another city"
    update_response = api_client.put(f"/contacts/update/{contact_id}", data=response.data, format="json")
    assert update_response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_create_contact_with_invalid_country(api_client):
    payload = {
        "email": "example@mail.com",
        "country": "fsdfsd",
        "city": "Moscow",
        "street": "test street",
        "house_number": 25,
    }
    response = api_client.post("/contacts/create", data=payload, format="json")
    assert response.status_code == status.HTTP_400_BAD_REQUEST

