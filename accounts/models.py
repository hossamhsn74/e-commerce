from django.db import models

# Create your models here.


class customer(models.Model):
    def __str__(self):
        return self.first_name

    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    email = models.EmailField(max_length=50, unique=True)
    mobile = models.IntegerField(null=True)
    password = models.CharField(max_length=50, null=False)
    country = models.CharField(max_length=50, null=True)
    state = models.CharField(max_length=50, null=True)
