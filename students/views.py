from django.shortcuts import render
from django.http import HttpResponse, FileResponse
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView, ListView
from .models import Student_Information
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
import os


class Create_student(LoginRequiredMixin, CreateView):
    model = Student_Information
    fields = ['school_id', 'year', 'reg_id', 'first_name', 'last_name', 'gender', 'father_name',
              'mother_name', 'date_of_birth_bs', 'date_of_birth_ad', 'disability',  'caste']

    def form_valid(self, form):
        form.instance.student = self.request.user
        return super().form_valid(form)
