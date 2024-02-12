from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "index_page.html")


def login(request):
    return render(request, "login_page.html")


def signup(request):
    return render(request, "signup_page.html")


def recipe(request):
    return render(request, "recipe_page.html")


def about(request):
    return render(request, "about_page.html")


def contact_us(request):
    return render(request, "contact_us_page.html")
