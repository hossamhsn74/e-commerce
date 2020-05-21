from django.shortcuts import render,HttpResponseRedirect,reverse,get_object_or_404
from .forms import user_form,profile_form,login_form
from django.contrib.auth.models import User
from .models import profile
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from cart.models import cart
# Create your views here.

def register(request):
    print("fdg")
    if request.method=='POST':
        userform=user_form(request.POST)
        profileform=profile_form(request.POST)
        if userform.is_valid() and profileform.is_valid():
            print("valid")
            username=userform.cleaned_data.get('username')
            first_name=userform.cleaned_data.get('first_name')
            last_name=userform.cleaned_data.get('last_name')
            email=userform.cleaned_data.get('email')
            password=userform.cleaned_data.get('password')
            phone_number=profileform.cleaned_data.get('phone_number')
            myuser=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
            image = request.FILES.get('image')
            myprofile=profile.objects.create(user=myuser, phone_number= phone_number)

            myprofile.image=image
            myprofile.save()
            login(request,myuser)

            new_cart = cart.objects.create(user =myuser )
            new_cart.save()

            return HttpResponseRedirect(reverse("account:login"))
        else:
            print("not valid")
            print(userform.errors)
            return render(request,"register.html",{'userform':userform})
    else:
        print("get")
        userform=user_form()
        profileform=profile_form()
        return render(request,'register.html',{'userform':user_form,'profileform':profileform})

def user_login(request):
    if request.method=='POST':
        loginform=login_form()
        # if loginform.is_valid():
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        print(user)
        if user is not None:
            login(request,user)
            print("loggedin")
            return HttpResponseRedirect(reverse("home"))
        else:
            print("not loggedin ")
            error="user doesn't exist"
            return render(request,"login.html",{'loginform':loginform,'error':error})

    else:
        loginform=login_form()
        return render(request,"login.html",{'loginform':loginform})

def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse("home"))

def user_profile(request,username):
    logged_user=request.user
    myuser=get_object_or_404(User,username=username)
    user_list=[]
    return render(request,"profile.html", {'user_data':myuser})


# def search_user(request,keyword):
    # # keyword=request.GET.get('keyword')
    # myusers=User.objects.filter(Q(username__icontains=keyword)|Q(first_name__icontains=keyword)|Q(last_name__icontains=keyword))
    # all_followings=request.user.followings.all()
    # mylist=[]
    # mydict={}
    # for following in all_followings:
    #     mylist.append(following.myuser)
    # for user in myusers:
    #     if user in mylist:
    #         mydict[user]=True
    #     else:
    #         mydict[user]=False
    #
    # return render(request,"search_user.html",{'myusers':myusers,'dict':mydict})


