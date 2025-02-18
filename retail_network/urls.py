from django.urls import path

from retail_network.apps import RetailNetworkConfig
from retail_network.views import (NetworkNodeCreateAPIView,
                                  NetworkNodeDeleteAPIView,
                                  NetworkNodeDetailAPIView,
                                  NetworkNodeUpdateAPIView)

app_name = RetailNetworkConfig.name

urlpatterns = [
    path("create", NetworkNodeCreateAPIView.as_view(), name="create"),
    path("delete/<int:node_id>", NetworkNodeDeleteAPIView.as_view(), name="delete"),
    path("<int:node_id>", NetworkNodeDetailAPIView.as_view(), name="detail"),
    path("update/<int:node_id>", NetworkNodeUpdateAPIView.as_view(), name="update"),
]
