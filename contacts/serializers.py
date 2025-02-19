from rest_framework import serializers

from contacts.models import Contact


class ContactInputSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Contact
        fields = "__all__"


class ContactUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        exclude = ["email"]


class ContactOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"
