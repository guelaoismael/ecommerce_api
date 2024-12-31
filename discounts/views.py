from django.shortcuts import render
from rest_framework import viewsets, permissions

from .models import Discount
from .serializers import DiscountSerializer

# REST API ViewSet providing CRUD operations for Discount model.
class DiscountViewSet(viewsets.ModelViewSet):
  queryset = Discount.objects.all()
  serializer_class = DiscountSerializer
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]