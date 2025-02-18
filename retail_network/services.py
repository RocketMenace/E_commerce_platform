from typing import Any

from django.http import Http404
from django.db import transaction
from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework.generics import get_object_or_404

from products.models import Product
from retail_network.models import NetworkNode


def create_node(data: dict[str, Any]) -> NetworkNode:
    with transaction.atomic():
        node = NetworkNode.objects.create(
            title=data["title"],
            contacts=data["contacts"],
            supplier=data.get("supplier", None),
        )
        products = Product.objects.bulk_create(
            [Product(**product) for product in data["products"]]
        )
        node.products.set(products)
        return node


def delete_node(node_id: int):
    try:
        contact = get_object_or_404(NetworkNode, id=node_id)
        contact.delete()
    except Http404:
        raise APIException(
            detail=f"Объект с {node_id=} не существует",
            code=status.HTTP_404_NOT_FOUND,
        )


def get_node(node_id: int):
    node = NetworkNode.objects.prefetch_related("contacts", "products", "supplier").get(
        pk=node_id
    )
    if not node:
        raise APIException(
            detail=f"Объект с {node_id=} не существует",
            code=status.HTTP_404_NOT_FOUND,
        )
    return node


def update_node(node_id: int, data: dict[str, Any]):
    node = NetworkNode.objects.filter(pk=node_id)
    if not node:
        raise APIException(
            detail=f"Объект с {node_id=} не существует",
            code=status.HTTP_404_NOT_FOUND,
        )
    node.update(**data)
    return node
