from django.shortcuts import render
from .models import products
from .models import CATEGORY_CHOISE


def productHome(request):
    data = products.objects.all()
    all_products = {"products": data}
    return render(request, 'products/product-home.html', context=all_products)


def details(request, id):
    for product in products.objects.all():
        if product.id == id:
            current_product = product
    return render(request, 'products/product-details.html', context={"current_product": current_product})
