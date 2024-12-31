from rest_framework import serializers
from .models import Order, OrderItem

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['id', 'order', 'product', 'quantity', 'price']
        

class OrderSerializer(serializers.ModelSerializer):
    # A nested serializer to represent all items in the order.
    items = OrderItemSerializer(many=True, read_only=True)
   
    #  A read-only field to display the total cost of the order,
    #  calculated dynamically from the associated OrderItem objects.
    total_amount = serializers.ReadOnlyField()
    
    class Meta:
        model = Order
        fields = ['id', 'created_date', 'user', 'total_amount', 'items']
