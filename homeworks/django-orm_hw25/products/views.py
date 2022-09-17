from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Category


def add_product(request):
    if request.user.is_authenticated:
        if request.method == "GET":
            return render(request, "products/add.html")
        else:
            product = Product()
            product.title = request.POST.get("title")
            product.description = request.POST.get("description")
            product.user = request.user
            product.save()
            return redirect("/")
    else:
        return redirect("/")


def product_details(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, "products/details.html", {"product": product})


def add_category(request):
    if request.user.is_authenticated and request.user.is_staff:
        if request.method == "POST":
            if request.POST.get("title"):
                category = Category()
                category.title = request.POST.get("title")
                category.save()
                return redirect("/")
        else:
            categories = Category.objects.order_by("-id")
            return render(request, "products/category/add.html",
                          {"categories": categories})


def category_details(request):
    categories = Category.objects.order_by("title")
    products = Product.objects.order_by("title")

    return render(request, 'products/category/details.html', {
        "categories": categories,
        "products": products
    })
