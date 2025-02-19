import pytest
from rest_framework import status


@pytest.mark.django_db
def test_create_product(api_client, create_product_for_test, login_user_for_tests):
    payload = {**create_product_for_test}
    response = api_client.post(
        "/products/create",
        data=payload,
        format="json",
        headers={"Authorization": "Bearer " + login_user_for_tests},
    )
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data.items() >= payload.items()


@pytest.mark.django_db
def test_get_product(api_client, create_product_for_test, login_user_for_tests):
    payload = {**create_product_for_test}
    response = api_client.post(
        "/products/create",
        data=payload,
        format="json",
        headers={"Authorization": "Bearer " + login_user_for_tests},
    )
    product_id = response.data["id"]
    get_response = api_client.get(
        f"/products/{product_id}",
        headers={"Authorization": "Bearer " + login_user_for_tests},
    )
    assert get_response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_delete_product(api_client, create_product_for_test, login_user_for_tests):
    payload = {**create_product_for_test}
    response = api_client.post(
        "/products/create",
        data=payload,
        format="json",
        headers={"Authorization": "Bearer " + login_user_for_tests},
    )
    product_id = response.data["id"]
    delete_response = api_client.delete(
        f"/products/delete/{product_id}",
        headers={"Authorization": "Bearer " + login_user_for_tests},
    )
    assert delete_response.status_code == status.HTTP_204_NO_CONTENT
