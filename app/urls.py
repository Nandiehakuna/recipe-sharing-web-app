from django.urls import path
from app import views


urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login, name="login"),
    path("signup/", views.signup, name="signup"),
    path("recipe/", views.recipe, name="recipe"),
    path("about/", views.about, name="about"),
    path("contact_us/", views.contact_us, name="contact_us"),
]
