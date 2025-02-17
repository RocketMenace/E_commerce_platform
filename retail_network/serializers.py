from rest_framework import serializers
from retail_network.models import NetworkNode


class NetworkNodeInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = NetworkNode
        fields = "__all__"

class NetworkNodeOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = NetworkNode
        fields = "__all__"