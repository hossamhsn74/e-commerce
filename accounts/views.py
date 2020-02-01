from django.shortcuts import render

# Create your views here.
def accountsHome(request):
    return render(request, 'accounts/signup.html')