from django.shortcuts import render
from django.http import HttpResponse, FileResponse
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView, ListView

from django.contrib.auth.mixins import LoginRequiredMixin


def bills_home(request):
    return render(request, "bills/bills_home.html")
