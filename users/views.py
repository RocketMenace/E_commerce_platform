from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from users.serializers import UserInputSerializer, UserOutputSerializer
from users.services import create_user, delete_user, get_user

# Create your views here.


class UserCreateAPIView(APIView):
    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "username": openapi.Schema(type=openapi.TYPE_STRING),
                "password": openapi.Schema(type=openapi.TYPE_STRING),
                "email": openapi.Schema(type=openapi.TYPE_STRING),
            },
            required=["username", "password", "email"],
        ),
        responses={
            201: openapi.Response("User registered successfully"),
            400: "Invalid input",
        },
    )
    def post(self, request):
        serializer = UserInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = create_user(serializer.validated_data)
        output_serializer = UserOutputSerializer(user)
        return Response(data=output_serializer.data, status=status.HTTP_201_CREATED)


class UserDeleteAPIView(APIView):
    def delete(self, request, user_id):
        delete_user(user_id)
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserDetailAPIView(APIView):
    def get(self, request, user_id):
        user = get_user(user_id)
        output_serializer = UserOutputSerializer(user)
        return Response(data=output_serializer.data, status=status.HTTP_200_OK)
