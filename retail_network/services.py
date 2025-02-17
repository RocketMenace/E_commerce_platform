from django.http import Http404
from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework.generics import get_object_or_404

from retail_network.models import NetworkNode
from typing import Any



def create_node(data: dict[str, Any]) -> NetworkNode:
    node = NetworkNode.objects.create(**data)
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
    try:
        return get_object_or_404(NetworkNode, id=node_id)
    except Http404:
        raise APIException(
            detail=f"Объект с {node_id=} не существует",
            code=status.HTTP_404_NOT_FOUND,
        )

def update_node(node_id: int, data: dict[str, Any]):
    node = NetworkNode.objects.filter(pk=node_id)
    if not node:
        raise APIException(
            detail=f"Объект с {node_id=} не существует",
            code=status.HTTP_404_NOT_FOUND,
        )
    node.update(**data)
    return node