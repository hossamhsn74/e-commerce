from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, reverse
from products.models import products
from .models import cart, cart_item
from django.contrib.auth.decorators import login_required


@login_required
def add(request, id):
    get_product = get_object_or_404(products, id=id)
    user = request.user
    mycart_item = cart_item.objects.create(myproduct=get_product)
    get_cart, created = cart.objects.get_or_create(user=user)
    print(mycart_item)
    print(get_cart.cart_items.all())

    x = get_cart.cart_items.filter(myproduct=mycart_item.myproduct)
    # if mycart_item not in get_cart.cart_items.all():
    if not x.exists():
        get_cart.cart_items.add(mycart_item)
    total = 0
    for item in get_cart.cart_items.all():
        item.total = item.myproduct.price * item.number
        item.save()
        total += item.myproduct.price * item.number

    get_cart.total = total
    get_cart.save()
    return HttpResponseRedirect(reverse("home"))


def display_cart(request):
    get_cart = get_object_or_404(cart, user=request.user)
    return render(request, "cart.html", {'cart': get_cart})


def remove_from_cart(request, id):
    user = request.user
    mycart = cart.objects.get(user=user)
    mycart_item = get_object_or_404(cart_item, id=id)
    mycart.cart_items.remove(mycart_item)
    # mycart.total-=mycart_item.product.price
    mycart.total -= mycart_item.total
    mycart.save()
    return HttpResponseRedirect(reverse('cart:display_cart'))


def update_number(request, id):
    mycart_item = get_object_or_404(cart_item, id=id)
    mycart_item.number = request.POST['number']
    mycart_item.save()
    mycart = get_object_or_404(cart, user=request.user)
    total = 0
    for item in mycart.cart_items.all():
        item.total = item.myproduct.price * item.number
        item.save()
        total += item.myproduct.price * item.number
    mycart.total = total
    mycart.save()

    print(mycart_item.number)
    print(id)
    print(request.POST['number'])
    return HttpResponseRedirect(reverse('cart:display_cart'))

#
# def charge(request):
#     print('charge==========================')
#     get_cart, created = cart.objects.get_or_create(user=request.user)
#     for item in get_cart:
#         request.user.profile.orders.add(item.myproduct)
#         request.user.profile.save()
#     return  render(request, 'charge.html')