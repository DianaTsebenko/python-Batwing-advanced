from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .models import MenuItem
from products.models import Product, Order, OrderItem
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
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
        total_price = 0
        for product_id in request.session.get("products", []):
            product_price = Product.objects.get(id=product_id).price
            total_price = total_price + product_price

        request.session["cart_total_price"] = total_price

    else:
        raise Http404()
    return redirect("/")


def cart(request):
    if request.session.get("products", False):
        products = Product.objects.filter(id__in=request.session.get("products"))
        return render(request, "main/cart.html", {"products": products, "total_price": request.session.get("cart_total_price", 0)})
    else:
        return render(request, "main/cart.html", {})


def remove_from_cart(request, product_id):
    if request.session.get("products", False):
        product_len = len(request.session.get("products"))
        for i in range(product_len):
            if request.session.get("products")[i] == product_id:
                del request.session.get("products")[i]
                request.session.modified = True
                product = Product.objects.get(id=product_id)
                request.session["cart_total_price"] = request.session["cart_total_price"] - product.price
                break
    return redirect("/cart")


def order(request):
    if request.session.get("products", False):
        if request.user.is_authenticated:
            if request.method == "GET":
                return render(request, "main/order.html", {"total_price": request.session.get("cart_total_price", 0)})
            else:
                order = Order()
                order.user = request.user
                order.message = request.POST.get("description")
                order.address = request.POST.get("address")
                order.name = request.POST.get("name")
                order.email = request.POST.get("email")
                order.total_price = request.session.get("cart_total_price")
                order.save()
                for product_id in request.session.get("products", []):
                    order_item = OrderItem()
                    order_item.order = order
                    order_item.product_id = product_id
                    order_item.save()

                send_mail(
                    "New Order #" + str(order.id),
                    "You have new order on the Our Shop \n Message from client: \n" + order.message,
                    "turupuru8@gmail.com",
                    ["lubomur.luzhnuy@gmail.com"],
                )
                request.session["products"] = []
                request.session["cart_total_price"] = 0
                return redirect("/")
