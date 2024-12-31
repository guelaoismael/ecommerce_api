from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AddWishlistView, ProductWishListView, WishlistDetail


urlpatterns = [
    path("products/<int:pk>/wishlists/add/", AddWishlistView.as_view(), name="add-wishlist"),
    path("wishlists/", ProductWishListView.as_view(), name="wishlist"),
    path("wishlists/<int:pk>/", WishlistDetail.as_view(), name="wishlist-detail"),
]


