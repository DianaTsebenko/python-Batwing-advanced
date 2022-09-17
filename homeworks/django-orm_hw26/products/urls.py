from itertools import product

from django.urls import path
from .views import add_products, product_details, edit_product

urlpatterns = [
    path("/add", add_products, name="add_product"),
    path("/<int:id>", product_details, name="product_details"),
    path("/edit_product/<int:id>", edit_product, name="edit_product"),

]