from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from products.serializers import (ProductInputSerializer,
                                  ProductOutputSerializer)
from products.services import (create_product, delete_product, get_product,
                               update_product)
from users.permissions import IsActive

# Create your views here.


class ProductCreateAPIView(APIView):
    permission_classes = [IsAuthenticated & IsActive]

    def post(self, request) -> Response:
        serializer = ProductInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if serializer.is_valid():
            product = create_product(serializer.validated_data)
            output_serializer = ProductOutputSerializer(product)
            return Response(data=output_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDeleteAPIView(APIView):
    permission_classes = [IsAuthenticated & IsActive]

    def delete(self, request, product_id) -> Response:
        delete_product(product_id)
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProductDetailView(APIView):
    permission_classes = [IsAuthenticated & IsActive]

    def get(self, request, product_id):
        product = get_product(product_id)
        output_serializer = ProductOutputSerializer(product)
        return Response(data=output_serializer.data, status=status.HTTP_200_OK)


class ProductUpdateAPIView(APIView):
    permission_classes = [IsAuthenticated & IsActive]

    def put(self, request, product_id):
        product = update_product(product_id, request.data)
        output_serializer = ProductOutputSerializer(product)
        return Response(data=output_serializer.data, status=status.HTTP_200_OK)
