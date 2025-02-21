from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from retail_network.models import NetworkNode
from retail_network.serializers import (NetworkNodeInputSerializer,
                                        NetworkNodeOutputSerializer)
from retail_network.services import (create_node, delete_node, get_node,
                                     update_node)
from users.permissions import IsActive

# Create your views here.


class NetworkNodeCreateAPIView(APIView):
    permission_classes = [IsAuthenticated & IsActive]

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "title": openapi.Schema(type=openapi.TYPE_STRING),
                "contacts": openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "email": openapi.Schema(type=openapi.TYPE_STRING),
                        "country": openapi.Schema(type=openapi.TYPE_STRING),
                        "city": openapi.Schema(type=openapi.TYPE_STRING),
                        "street": openapi.Schema(type=openapi.TYPE_STRING),
                        "house_number": openapi.Schema(type=openapi.TYPE_STRING),
                    },
                ),
                "products": openapi.Schema(
                    type=openapi.TYPE_ARRAY,
                    items=openapi.Schema(
                        type=openapi.TYPE_OBJECT,
                        properties={
                            "name": openapi.Schema(type=openapi.TYPE_STRING),
                            "model": openapi.Schema(type=openapi.TYPE_STRING),
                            "release_date": openapi.Schema(
                                type=openapi.TYPE_STRING, format="date"
                            ),
                        },
                    ),
                ),
                "supplier": openapi.Schema(type=openapi.TYPE_INTEGER),
                "debt": openapi.Schema(type=openapi.TYPE_NUMBER),
            },
            required=["title", "contacts", "products"],
        ),
        responses={
            201: openapi.Response("Network node created successfully"),
            400: "Invalid input",
        },
    )
    def post(self, request):
        serializer = NetworkNodeInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        node = create_node(serializer.validated_data)
        output_serializer = NetworkNodeOutputSerializer(node)
        return Response(data=output_serializer.data, status=status.HTTP_201_CREATED)


class NetworkNodeDeleteAPIView(APIView):
    permission_classes = [IsAuthenticated & IsActive]

    def delete(self, request, node_id):
        delete_node(node_id)
        return Response(status=status.HTTP_204_NO_CONTENT)


class NetworkNodeDetailAPIView(APIView):
    permission_classes = [IsAuthenticated & IsActive]

    def get(self, request, node_id):
        node = get_node(node_id)
        output_serializer = NetworkNodeOutputSerializer(node)
        return Response(data=output_serializer.data, status=status.HTTP_200_OK)


class NetworkNodeUpdateAPIView(APIView):
    # permission_classes = [IsAuthenticated & IsActive]

    def put(self, request, node_id):
        serializer = NetworkNodeInputSerializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        node = update_node(node_id, serializer.validated_data)
        output_serializer = NetworkNodeOutputSerializer(node, partial=True)
        return Response(data=output_serializer.data, status=status.HTTP_200_OK)


class NetworkNodeListAPIView(ListAPIView):
    permission_classes = [IsAuthenticated & IsActive]
    queryset = NetworkNode.objects.all().prefetch_related("contacts")
    serializer_class = NetworkNodeOutputSerializer
    filter_backends = [
        SearchFilter,
    ]
    search_fields = ["contacts__country"]
