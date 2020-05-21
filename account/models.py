from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse
from products.models import products
from orders.models import Order
import datetime
# Create your models here.


class profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='images/')
    phone_number =  models.IntegerField(null=True, blank=True)
    orders = models.ManyToManyField(Order, related_name='profile_orders' , blank=True)


    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse("account:profile",kwargs={'username':self.user.username})


