from django.urls import path

from products.apps import ProductsConfig
from products.views import (
    ProductCreateAPIView,
    ProductDeleteAPIView,
    ProductDetailView,
    ProductUpdateAPIView,
)

app_name = ProductsConfig.name

urlpatterns = [
    path("create", ProductCreateAPIView.as_view(), name="create"),
    path("delete/<int:product_id>", ProductDeleteAPIView.as_view(), name="delete"),
    path("<int:product_id>", ProductDetailView.as_view(), name="detail"),
    path("update/<int:product_id>", ProductUpdateAPIView.as_view(), name="update"),
]
