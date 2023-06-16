from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("register/", views.register, name="register_user"),
    path('login/', views.login_view, name='login'),
]
