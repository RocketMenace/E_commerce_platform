from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from retail_network.serializers import (NetworkNodeInputSerializer,
                                        NetworkNodeOutputSerializer)
from retail_network.services import (create_node, delete_node, get_node,
                                     update_node)

# Create your views here.


class NetworkNodeCreateAPIView(APIView):
    def post(self, request):
        serializer = NetworkNodeInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        node = create_node(serializer.validated_data)
        output_serializer = NetworkNodeOutputSerializer(node)
        return Response(data=output_serializer.data, status=status.HTTP_201_CREATED)


class NetworkNodeDeleteAPIView(APIView):
    def delete(self, request, node_id):
        delete_node(node_id)
        return Response(status=status.HTTP_204_NO_CONTENT)


class NetworkNodeDetailAPIView(APIView):
    def get(self, request, node_id):
        node = get_node(node_id)
        output_serializer = NetworkNodeOutputSerializer(node)
        return Response(data=output_serializer.data, status=status.HTTP_200_OK)


class NetworkNodeUpdateAPIView(APIView):
    def put(self, request, node_id):
        serializer = NetworkNodeInputSerializer(data=request.data, partial=True)
        node = update_node(node_id, serializer.validated_data)
        output_serializer = NetworkNodeOutputSerializer(node)
        return Response(data=output_serializer.data, status=status.HTTP_200_OK)
