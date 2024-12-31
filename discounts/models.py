from django.db import models
from products.models import Product
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator

# Model that handles product price discounts with time-based activation.

class Discount(models.Model):
  
  product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="discounts")
  percentage = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(100)])
  start_date = models.DateTimeField()
  end_date = models.DateTimeField()
  
  # Checks if discount is currently valid based on start/end dates.
  def is_active(self):
    now = timezone.localtime(timezone.now())
    return self.start_date <= now <= self.end_date
  
  # Applies discount percentage to given price if discount is active.
  def apply_discount(self, price):
    if self.is_active():
      return price * (1 - self.percentage / 100)
    return price
 