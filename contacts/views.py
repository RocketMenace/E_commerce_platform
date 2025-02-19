from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from contacts.serializers import (ContactInputSerializer,
                                  ContactOutputSerializer)
from contacts.services import (create_contact, delete_contact, get_contact,
                               update_contact)
from users.permissions import IsActive

# Create your views here.


class ContactCreateAPIView(APIView):
    permission_classes = [IsAuthenticated & IsActive]

    def post(self, request) -> Response:
        serializer = ContactInputSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            contact = create_contact(serializer.validated_data)
            output_serializer = ContactOutputSerializer(contact)
            return Response(data=output_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ContactDeleteAPIView(APIView):
    permission_classes = [IsAuthenticated & IsActive]

    def delete(self, request, contact_id) -> Response:
        delete_contact(contact_id)
        return Response(status=status.HTTP_204_NO_CONTENT)


class ContactDetailAPIView(APIView):
    permission_classes = [IsAuthenticated & IsActive]

    def get(self, request, contact_id) -> Response:
        contact = get_contact(contact_id)
        output_serializer = ContactOutputSerializer(contact)
        return Response(output_serializer.data, status.HTTP_200_OK)


class ContactUpdateAPIView(APIView):
    permission_classes = [IsAuthenticated & IsActive]

    def put(self, request, contact_id):
        contact = update_contact(contact_id, request.data)
        output_serializer = ContactOutputSerializer(contact, partial=True)
        return Response(data=output_serializer.data, status=status.HTTP_200_OK)
