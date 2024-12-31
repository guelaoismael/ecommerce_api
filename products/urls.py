from django.urls import path, include
from .views import ( ProductImageViewSet, ProductViewSet, CategoryViewSet, CreateReview, 
                    ProductReviewList, ReviewList, ReviewDetail )

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r"products", ProductViewSet, basename="product")
router.register(r"categories", CategoryViewSet, basename="category")
router.register(r"product-images", ProductImageViewSet, basename="image")

 

urlpatterns = [
    path("", include(router.urls)),
    path("products/<int:pk>/reviews/new/", CreateReview.as_view(), name="new-review"),
    path("products/<int:pk>/reviews/", ProductReviewList.as_view(), name="product-reviews"),
    path("reviews/", ReviewList.as_view(), name="review-list"),
    path("reviews/<int:pk>/", ReviewDetail.as_view(), name="review-detail"),
]
