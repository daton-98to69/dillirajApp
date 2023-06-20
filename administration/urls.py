from django.urls import path
from . import views

app_name = "administration"
urlpatterns = [
    path("dashboard/", views.dashboard, name="admin_dashboard"),
    path("announcement/", views.announce, name="announcement"),
]
