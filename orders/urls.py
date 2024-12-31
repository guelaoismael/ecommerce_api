from django.urls import path, include
from .views import OrderItemViewSet, OrderViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r"order/items", OrderItemViewSet, basename="order-item")
router.register(r"orders", OrderViewSet, basename="order")

urlpatterns = [
    path("", include(router.urls)),
]
