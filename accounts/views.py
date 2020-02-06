from django.shortcuts import render
from .forms import my_form
from .models import customer
from django.http import HttpResponseRedirect


def index(request):
    return render(request, 'products/product-home.html', {'name': 'laila'})


def login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        customer_list = customer.objects.filter(email=email)

        for i in customer_list:
            if i.email == email:
                print('you are log in')
                break
            else:
                print('you are not logged in')
    return render(request, 'accounts/login.html', {'name': 'laila'})


def signup(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        mobile = request.POST['mobile']
        password = request.POST['password']
        country = request.POST['country']
        state = request.POST['country']

        customer.objects.create(first_name=first_name, last_name=last_name,
                                email=email, mobile=mobile, password=password)
        return HttpResponseRedirect('/login')
    return render(request, 'accounts/signup.html')
