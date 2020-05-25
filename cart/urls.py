#
from django.urls import path
from . import views
app_name='cart'
urlpatterns = [
    path('add/<int:id>/', views.add,name='add'),
    path('display_cart/', views.display_cart,name='display_cart'),
    path('update_number/<int:id>/', views.update_number,name='update_number'),
    path('remove/<int:id>/', views.remove_from_cart,name='remove_from_cart'),
]
