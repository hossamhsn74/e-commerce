import stripe
from cart.models import cart,cart_item
from orders.models import Order
from django.conf import settings
from django.views.generic.base import TemplateView
from django.shortcuts import render # new

stripe.api_key = settings.STRIPE_SECRET_KEY # new

class HomePageView(TemplateView):
    template_name = 'cart.html'

    def get_context_data(self, **kwargs):  # new
        context = super().get_context_data(**kwargs)
        context['key'] = settings.STRIPE_PUBLISHABLE_KEY
        return context


def charge(request): # new
    if request.method == 'POST':
        print('charge==========================')
        get_cart, created = cart.objects.get_or_create(user=request.user)
        new_order=Order.objects.create(user_ordered=request.user)
        for item in get_cart.cart_items.all():
            new_order.items.add(item)
            new_order.save()
            request.user.profile.orders.add(new_order)
            print(item)
            request.user.profile.save()
            get_cart.cart_items.remove(item)
        get_cart.save()

        charge = stripe.Charge.create(
            amount=get_cart.total,
            currency='usd',
            description='A Django charge',
            source=request.POST['stripeToken']
        )
        return render(request, 'charge.html')
