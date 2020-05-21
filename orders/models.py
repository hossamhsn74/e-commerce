from django.db import models
from django.contrib.auth.models import User
from cart.models  import cart_item
# Create your models here.

class Order(models.Model):
    user_ordered = models.ForeignKey(User, on_delete=models.CASCADE, related_name='all_orders')
    items = models.ManyToManyField(cart_item ,related_name='items_orders')
