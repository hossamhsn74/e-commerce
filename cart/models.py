from django.db import models
from products.models import products
from django.contrib.auth.models import User

# Create your models here.

class cart_item(models.Model):
    myproduct=models.ForeignKey(products,on_delete=models.CASCADE,related_name='items')
    number=models.IntegerField(default=1)
    total=models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.myproduct.name


class cart(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    cart_items = models.ManyToManyField('cart_item',related_name='carts',blank=True)
    total=models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.user.username

