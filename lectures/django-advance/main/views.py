from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .models import MenuItem
from products.models import Product
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q


def home(request):
    menu_items = MenuItem.objects.all()
    products = Product.objects.filter(display_on_main_page=True, approved=True).order_by("-id")
    return render(request, 'main/index.html', {
        "menu_items": menu_items,
        "products": products
    })


def sign_up(request):
    if request.method == "POST":
        user = User()
        user.username = request.POST.get("username")
        user.email = request.POST.get("email")
        user.set_password(request.POST.get("password"))
        user.first_name = request.POST.get("first_name")
        user.last_name = request.POST.get("last_name")
        user.is_superuser = False
        user.is_staff = False
        user.is_active = True
        user.save()
        login(request, user)
        return redirect("/")
    else:
        return render(request, "main/sign-up.html", {})


def sign_in(request):
    if request.method == "POST":
        user = authenticate(request, username=request.POST.get("username"), password=request.POST.get("password"))
        print("================USER ===============")
        print(user)
        if user:
            login(request, user)
        return redirect("/")
    else:
        return render(request, "main/sign-in.html", {})


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect("/")


def add_to_cart(request, product_id):
    if Product.objects.get(id=product_id):
        if product_id in request.session.get("products", []):
            return redirect("/")
        if request.session.get("products", False):
            request.session["products"].append(product_id)
            request.session.modified = True
        else:
            request.session["products"] = []
            request.session["products"].append(product_id)
    else:
        raise Http404()
    return redirect("/")


def cart(request):
    if request.session.get("products", False):
        products = Product.objects.filter(id__in=request.session.get("products"))
        return render(request, "main/cart.html", {"products": products})
    else:
        return render(request, "main/cart.html", {})


def remove_from_cart(request, product_id):
    if request.session.get("products", False):
        product_len = len(request.session.get("products"))
        for i in range(product_len):
            if request.session.get("products")[i] == product_id:
                del request.session.get("products")[i]
                request.session.modified = True
                break
    return redirect("/cart")