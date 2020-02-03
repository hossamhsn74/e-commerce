from django.db import models

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
    category = models.CharField(max_length=50, choices=CATEGORY_CHOISE, default='NEW' )    
    isNew = models.BooleanField(default='False')
    isBestSeller = models.BooleanField(default='False')
