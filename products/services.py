from typing import Any

from django.db import IntegrityError
from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.exceptions import APIException

from products.models import Product


def create_product(data: dict[str, Any]):
    try:
        product = Product.objects.create(**data)
        return product
    except IntegrityError:
        raise APIException(
            detail="release_date не может быть меньше текущего времени",
            code=status.HTTP_400_BAD_REQUEST,
        )


def delete_product(product_id: int):
    try:
        contact = get_object_or_404(Product, id=product_id)
        contact.delete()
    except Http404:
        raise APIException(
            detail=f"Продукт с {product_id=} не существует",
            code=status.HTTP_404_NOT_FOUND,
        )


def get_product(product_id: int):
    try:
        return get_object_or_404(Product, id=product_id)
    except Http404:
        raise APIException(
            detail=f"Продукт с {product_id=} не существует",
            code=status.HTTP_404_NOT_FOUND,
        )


def update_product(product_id: int, data: dict[str, Any]):
    product = Product.objects.filter(pk=product_id)
    if not product:
        raise APIException(
            detail=f"Контакт с {product_id=} не существует",
            code=status.HTTP_404_NOT_FOUND,
        )
    product.update(**data)
    return product
