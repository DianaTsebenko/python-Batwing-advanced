from django.shortcuts import render, redirect

from .models import MenuItem
from products.models import Product

from django.contrib.auth import authenticate, login, logout
from .forms import SignInForm, SignUpForm


def home(request):
    menu_items = MenuItem.objects.all()
    products = Product.objects.filter(display_on_main_page=True, approved=True).order_by("-id")
    print(request.user)
    return render(request, 'main/index.html', {
        "menu_items": menu_items,
        "products": products
    })


def sign_up(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data.get("password"))
            user = form.save()
            login(request, user)
            return redirect("/")
        else:
            return render(request, "main/sign-up.html", {"form": form})
    else:
        return render(request, "main/sign-up.html", {})


def sign_in(request):
    if request.method == "POST":
        form = SignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
        return render(request, "main/sign-in.html", {"form": form})
    else:
        return render(request, "main/sign-in.html", {})


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect("/")