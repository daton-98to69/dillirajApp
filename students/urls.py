from django.urls import path
from . import views
from .views import Create_student

app_name = "students"

urlpatterns = [
    path("new/", Create_student.as_view(), name="student_create"),


]
