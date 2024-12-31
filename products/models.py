from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
from django.utils import timezone



class Category(models.Model):
  """
    Represents a category for grouping related products.
  """
  name = models.CharField(max_length=100)
  description = models.TextField()
  created_date = models.DateTimeField(auto_now_add=True)
  updated_date = models.DateTimeField(auto_now=True)

  def __str__(self):
    """
    Returns a string representation of the category, typically its name.
    """
    return self.name

class Product(models.Model):
  """
    Represents a product within a category.
  """

  name = models.CharField(max_length=100, blank=False, null=False)
  description = models.TextField(blank=True)
  price = models.FloatField()
  stock_quantity = models.PositiveIntegerField(validators=[MinValueValidator(0, message="Stock quantity cannot be negatif")])
  category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
  created_date = models.DateTimeField(auto_now_add=True)
  updated_date = models.DateTimeField(auto_now=True)

  @property
  def discount_price(self):
    """
      Calculates and returns the discounted price if there is an active discount.
    """
    now = timezone.localtime(timezone.now())
    active_discount = self.discounts.filter(start_date__lte=now, end_date__gte=now).first()
    if active_discount:
      return active_discount.apply_discount(self.price)
    return self.price
  
  def reduce_stock_quantity(self, quantity):
    """
      Reduces the stock quantity of the product by the specified amount.
      Raises a ValueError if the stock is insufficient.
    """
    if self.stock_quantity >= quantity:
      self.stock_quantity -= quantity
      self.save()
    else:
      raise ValueError("Stock insufficient")

  def __str__(self):
    """
        Returns a string representation of the product, typically its name.
    """
    return self.name


class ProductImage(models.Model):
    """
      Represents an image associated with a product.
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="products/")
    is_main = models.BooleanField(default=False)

    def image_url(self):
        """
        Returns the URL of the uploaded image.
        """
        return self.image.url


class Review(models.Model):
  """
    Represents a user review for a product.
  """
  product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="reviews")
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
  comment = models.TextField(blank=True)
  created_date = models.DateTimeField(auto_now_add=True)
  updated_date = models.DateTimeField(auto_now=True)


