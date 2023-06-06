from django.urls import path
from . import views

app_name = "students"

urlpatterns = [
    path("dashboard/", views.dashboard, name="student_dashboard")
]
