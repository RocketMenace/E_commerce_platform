import pytest
from rest_framework import status
from datetime import datetime, timezone, timedelta


@pytest.mark.django_db
def test_create_retail_network(
    api_client, login_user_for_tests, create_contact_for_test_in_api
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
    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db
def test_get_retail_network(
    api_client, login_user_for_tests, create_retail_network_for_tests
):
    response = api_client.get(
        f"/retail_network/{create_retail_network_for_tests['id']}",
        headers={"Authorization": "Bearer " + login_user_for_tests},
    )
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_delete_retail_network(
    api_client, login_user_for_tests, create_retail_network_for_tests
):
    response = api_client.delete(
        f"/retail_network/delete/{create_retail_network_for_tests['id']}",
        headers={"Authorization": "Bearer " + login_user_for_tests},
    )
    assert response.status_code == status.HTTP_204_NO_CONTENT


@pytest.mark.django_db
def test_update_retail_network(
    api_client, login_user_for_tests, create_retail_network_for_tests
):
    payload = {"country": "US"}
    update_response = api_client.put(
        f"/retail_network/update/{create_retail_network_for_tests['id']}",
        data=payload,
        format="json",
        headers={"Authorization": "Bearer " + login_user_for_tests},
    )
    assert update_response.status_code == status.HTTP_200_OK
