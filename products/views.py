from django.shortcuts import render,HttpResponseRedirect,reverse
from .models import products
from .models import CATEGORY_CHOISE
from django.db.models import Q
from .models import Comment

def productHome(request):
    mobile_data = products.objects.filter(category='mobiles')
    new_data = products.objects.filter(category='new')
    electronics_data = products.objects.filter(category='electronics')
    home_data = products.objects.filter(category='home')
    bh_data = products.objects.filter(category='beauty & health')
    baby_data = products.objects.filter(category='baby')
    fashion_data = products.objects.filter(category='fashion')
    market_data = products.objects.filter(category='our market')
    deals_data = products.objects.filter(category='hot deals')
    return render(request, 'index.html',
                  {'mobile_data': mobile_data, 'new_data': new_data, 'electronics_data': electronics_data,
                   'home_data': home_data, 'bh_data': bh_data, 'baby_data': baby_data, 'fashion_data': fashion_data,
                   'market_data': market_data, 'deals_data': deals_data})


def details(request, id):
    for product in products.objects.all():
        if product.id == id:
            current_product = product
    return render(request, 'product-details.html', context={"current_product": current_product})


def search_product(request):
    keyword=request.GET.get('keyword')
    myproducts=products.objects.filter(Q(name__icontains=keyword)|Q(descreption__icontains=keyword)|Q(category__icontains=keyword))
    return render(request,"search.html",{'products':myproducts})

def search_category(request,category):
    data = products.objects.filter(category=category)
    category_list = {"products": data}
    return render(request, 'search.html', context=category_list)

def comment_product(request,id):
    print("hey-------")
    text=request.POST['text']
    print(text)
    myproduct=products.objects.get(id=id)
    new_comment=Comment.objects.create(text=text,product_comment=myproduct, user=request.user)
    new_comment.save()
    return HttpResponseRedirect(reverse("details",kwargs={'id':id}))
