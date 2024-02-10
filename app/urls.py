from django.urls import path
from app import views


urlpatterns = [
    path('',views.index, name="index"),
    path('login/',views.login, name="login"),
    path('signup/',views.signup, name="signup"),

]