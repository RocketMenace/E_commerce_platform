from rest_framework import serializers

from products.models import Product


class ProductInputSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Product
        fields = "__all__"


class ProductUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ["model"]


class ProductOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
