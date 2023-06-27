from django.urls import path
from . import views
from .views import SchoolInfo

app_name = "administration"
urlpatterns = [
    path("schoolinfo/", SchoolInfo.as_view(), name="school_info"),
    path("announcement/", views.announce, name="announcement"),
]
