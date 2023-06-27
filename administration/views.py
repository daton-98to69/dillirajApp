from django.shortcuts import render
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from django.contrib.auth.decorators import login_required
from accounts.models import CustomUser
from .models import Announcement, School_Information
from django.views.generic import DetailView, ListView

# Create your views here.


class SchoolInfo(ListView):
    model = School_Information
    template_name = "administration/schoolinfo.html"
    context_object_name = "school_info"


@login_required
def dashboard(request):
    user = request.user

    context = {
        'user': user
    }
    return render(request, "administration/dashboard.html", context)


@login_required
def announce(request):
    announce = Announcement.objects.filter(
        is_public=True).order_by('-date_posted')
    return render(request, "administration/announcement.html", {'announce': announce})
