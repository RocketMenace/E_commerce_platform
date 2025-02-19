from rest_framework import serializers

from contacts.models import Contact
from contacts.serializers import ContactOutputSerializer
from products.serializers import (ProductInputSerializer,
                                  ProductOutputSerializer)
from retail_network.models import NetworkNode


class SupplierOutputSerializer(serializers.ModelSerializer):
    contacts = serializers.SerializerMethodField()

    class Meta:
        model = NetworkNode
        fields = ["title", "contacts"]

    def get_contacts(self, obj):
        return ContactOutputSerializer(obj.contacts).data


class NetworkNodeInputSerializer(serializers.ModelSerializer):
    title = serializers.CharField()
    contacts = serializers.PrimaryKeyRelatedField(queryset=Contact.objects.all())
    supplier = serializers.PrimaryKeyRelatedField(
        queryset=NetworkNode.objects.all(), required=False, default=None
    )
    products = ProductInputSerializer(many=True, required=False)

    class Meta:
        model = NetworkNode
        fields = ["title", "contacts", "supplier", "products"]


class NetworkNodeOutputSerializer(serializers.ModelSerializer):
    contacts = serializers.SerializerMethodField()
    products = serializers.SerializerMethodField()
    supplier = serializers.SerializerMethodField()

    class Meta:
        model = NetworkNode
        fields = "__all__"
        read_only_fields = ["id", "created_at"]

    def get_contacts(self, obj):
        return ContactOutputSerializer(obj.contacts).data

    def get_products(self, obj):
        products = obj.products.all()
        return ProductOutputSerializer(products, many=True).data

    def get_supplier(self, obj):
        return SupplierOutputSerializer(obj.supplier).data
