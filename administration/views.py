from django.shortcuts import render
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from django.contrib.auth.decorators import login_required
from accounts.models import CustomUser

# Create your views here.


@login_required
def dashboard(request):
    user = request.user

    context = {
        'user': user
    }
    return render(request, "administration/dashboard.html", context)
