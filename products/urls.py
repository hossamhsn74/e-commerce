from django.urls import path
from products import views

urlpatterns = [
    path('', views.productHome, name='home'),
    path("<int:id>",views.details, name="details"),
    path("search",views.search_product,name='search'),
    path("<str:category>",views.search_category,name='category'),
    path("comments/<int:id>/", views.comment_product, name="comment"),
 ]
