from rest_framework import viewsets, filters, generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.validators import ValidationError

from .paginations import ProductPagination
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .models import Product, Category, ProductImage, Review
from .serializers import  ProductImageSerializer, ProductSerializer, CategorySerializer,ReviewSerializer

# Create your views here.

class ProductViewSet(viewsets.ModelViewSet):
  
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  filter_backends = [DjangoFilterBackend, filters.SearchFilter]
  filterset_fields = ['category', 'stock_quantity', 'price']
  search_fields = ['name', 'category__name']
  permission_classes = [IsAdminOrReadOnly]
  pagination_class = ProductPagination
  

class CategoryViewSet(viewsets.ModelViewSet):
  
  queryset = Category.objects.all()
  serializer_class = CategorySerializer
  permission_classes = [IsAdminOrReadOnly]


class CreateReview(generics.CreateAPIView):
  
  queryset = Review.objects.all()
  serializer_class = ReviewSerializer
  permission_classes = {permissions.IsAuthenticated}

  def perform_create(self, serializer):
    pk = self.kwargs.get('pk')
    product = Product.objects.get(pk=pk)

    review_user = self.request.user
    review_queryset = Review.objects.filter(product=product, user=review_user)

    if review_queryset.exists():
      raise ValidationError("You have already reviewed this product!")

    serializer.save(product=product, user=review_user)
  
class ProductReviewList(generics.ListAPIView):
    
  serializer_class = ReviewSerializer

  def get_queryset(self):
        
    pk = self.kwargs['pk']
    return Review.objects.filter(product=pk)


class ReviewList(generics.ListAPIView):
  
  queryset = Review.objects.all()
  serializer_class = ReviewSerializer

class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
  
  queryset = Review.objects.all()
  serializer_class = ReviewSerializer
  permission_classes = [IsOwnerOrReadOnly]


class ProductImageViewSet(viewsets.ModelViewSet):
  queryset = ProductImage.objects.all()
  serializer_class = ProductImageSerializer
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]