from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User
from products.models import Product

class Order(models.Model):

  """
    Represents a customer order, associated with a user and containing multiple items.
  """
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
  created_date = models.DateTimeField(auto_now_add=True)
  
  @property
  def total_amount(self):
    total = sum(item.price for item in self.items.all())
    return total
  
class OrderItem(models.Model):
  """
    Represents an individual item within an order, linked to a specific product.
  """

  order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
  product = models.ForeignKey(Product, on_delete=models.CASCADE)
  quantity = models.PositiveIntegerField(validators=[MinValueValidator(1)])
  price = models.FloatField(validators=[MinValueValidator(0)], default=0)

  def save(self, *args, **kwargs):
    """
        Overrides the default save method to:
        - Calculate and set the item's price based on the product price and quantity.
        - Reduce the stock of the associated product.
    """

    if self.product.stock_quantity < self.quantity:
      raise ValueError("Not enough stock available")
    
    self.price = self.product.price * self.quantity
    
    self.product.reduce_stock_quantity(self.quantity)
    super().save(*args, **kwargs)