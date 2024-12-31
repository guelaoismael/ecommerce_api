from django.shortcuts import render
from rest_framework import viewsets, filters, generics, permissions
from .models import Order, OrderItem
from .serializers import OrderSerializer, OrderItemSerializer

# Create your views here.
class OrderItemViewSet(viewsets.ModelViewSet):
  queryset = OrderItem.objects.all()
  serializer_class = OrderItemSerializer
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class OrderViewSet(viewsets.ModelViewSet):
  queryset = Order.objects.all()
  serializer_class = OrderSerializer
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]
