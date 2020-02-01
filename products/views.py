from django.shortcuts import render

# Create your views here.
def productHome(request):
    return render(request, 'products/product-home.html')