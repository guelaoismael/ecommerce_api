from rest_framework.validators import ValidationError
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework import views, permissions, status, generics
from products.models import Product
from .models import Wishlist
from .serializers import WishlistSerializer


class AddWishlistView(views.APIView):
  
  permission_classes = [permissions.IsAuthenticated]

  def post(self, request, pk):
    
    try:
      # Try to retrieve the product by its primary key.
      product = Product.objects.get(pk=pk)

    except Product.DoesNotExist():
      # Raise a 404 error if the product is not found.
      raise NotFound("This product doesn't exist")
      
    # Check if the product is already in the user's wishlist.
    if Wishlist.objects.filter(user=request.user, product=product).exists():
        raise ValidationError("This product is already in your wishlist.")
    
    # Add the product to the user's wishlist.
    Wishlist.objects.create(user=request.user, product=product)

    # Return a success message.
    return Response(
      {
        "message": "Product successfully added to wishlist."
      },
      status=status.HTTP_201_CREATED
    )
  
class ProductWishListView(generics.ListAPIView):

  """
    API endpoint to list all products in the authenticated user's wishlist.
  """ 
  serializer_class = WishlistSerializer
  permission_classes =[permissions.IsAuthenticated]

  def get_queryset(self):

    """
       Filters the wishlist items to only include those belonging to the authenticated user.
    """
        
    user = self.request.user
    return Wishlist.objects.filter(user=user)

class WishlistDetail(generics.RetrieveUpdateDestroyAPIView):
  
  """
     API endpoint for retrieving, updating, or deleting a specific wishlist item.
  """
  serializer_class = WishlistSerializer
  permission_classes =[permissions.IsAuthenticated]

  def get_queryset(self):

    """
     Filters the wishlist items to only include those belonging to the authenticated user.
    """   
    user = self.request.user
    return Wishlist.objects.filter(user=user)