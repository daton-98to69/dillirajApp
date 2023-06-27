from django.urls import path
from . import views


urlpatterns = [
    path("", views.bills_home, name="bills_home"),
]
