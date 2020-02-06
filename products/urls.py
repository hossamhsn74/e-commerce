from django.urls import path
from products import views
urlpatterns = [
    path('', views.productHome),
    path("<int:id>",views.details, name="details"),

]
