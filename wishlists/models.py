from django.db import models
from products.models import Product
from django.contrib.auth.models import User



# Create your models here.
class Wishlist(models.Model):
  product = models.ForeignKey(Product, on_delete=models.CASCADE)
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="wishlist")
  created_date = models.DateTimeField(auto_now_add=True)
  