from rest_framework import serializers
from .models import Discount

class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = ['id', 'product', 'percentage', 'start_date', 'end_date']