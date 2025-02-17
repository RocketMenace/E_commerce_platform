from rest_framework import serializers

from contacts.models import Contact


class ContactInputSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Contact
        fields = "__all__"

    # def update(self, instance, validated_data):
    #     if instance.email == validated_data.get("email", instance.email):
    #         validated_data.pop("email", None)
    #     for attr, value in validated_data.items():
    #         setattr(instance, attr, value)
    #     instance.save()
    #     return instance


class ContactOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"
