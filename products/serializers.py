from rest_framework import serializers
from .models import Product, Category, ProductImage, Review
from discounts.serializers import DiscountSerializer


class ReviewSerializer(serializers.ModelSerializer):
  """
    Serializer for the Review model.
  """
  class Meta :
    model = Review
    # fields = "__all__"
    exclude = ['product', 'user']

class CategorySerializer(serializers.ModelSerializer):
  """
    Serializer for the Category model.
  """
  class Meta :
    model = Category
    fields = "__all__"


class ProductImageSerializer(serializers.ModelSerializer):
    """
    Serializer for the ProductImage model.
    """

    # image_url: retrieve the URL of the image file.
    image_url = serializers.SerializerMethodField()

    class Meta:
      model = ProductImage
      fields = ['id', 'image_url', 'is_main']

    def get_image_url(self, obj):
        """
        Retrieves the URL of the image associated with this ProductImage instance.
        """
        return obj.image_url()
    
class ProductSerializer(serializers.ModelSerializer):
  
  #  A nested serializer to represent all reviews related to the product.
  reviews = ReviewSerializer(many=True, read_only=True)

  # A nested serializer to display active or past discounts for the product.
  discounts = DiscountSerializer(many=True, read_only=True)

  # A nested serializer to represent all images associated with the product.
  images = ProductImageSerializer(many=True, read_only=True)

  # A read-only field to display the calculated discounted price if applicable.
  discount_price = serializers.ReadOnlyField()

  class Meta :
    model = Product
    fields = ['id', 'category', 'name', 'description', 'price', 'discount_price', 'stock_quantity', 'images', 'discounts', 'reviews']

