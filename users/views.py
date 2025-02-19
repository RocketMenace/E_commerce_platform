from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from users.serializers import UserInputSerializer, UserOutputSerializer
from users.services import create_user, delete_user, get_user

# Create your views here.


class UserCreateAPIView(APIView):
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
