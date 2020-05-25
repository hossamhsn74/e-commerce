from django.db import models
from django.contrib.auth.models import User
CATEGORY_CHOISE = (
    ('new', 'NEW'),
    ('electronics', 'ELECTRONICS'),
    ('mobiles', 'MOBILES'),
    ('home', 'HOME'),
    ('beauty & health', 'BEAUTY & HEALTH'),
    ('baby', 'BABY'),
    ('fashion', 'FASHION'),
    ('our market', 'OUR MARKET'),
    ('hot deals', 'HOT DEALS'),
)


class products(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=100)
    descreption = models.TextField()
    price = models.PositiveIntegerField()    
    image = models.ImageField(upload_to="images/", default='static/images/The_Fresh_Market_logo.svg')
    category = models.CharField(max_length=50, choices=CATEGORY_CHOISE, default='NEW', null=True, blank=True)
    isNew = models.BooleanField(default='False')
    isBestSeller = models.BooleanField(default='False')

class Comment(models.Model):
    product_comment = models.ForeignKey(products, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comments', blank=True)

    def __str__(self):
        return self.text
