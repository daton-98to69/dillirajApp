from django.db import models
from accounts.models import CustomUser
# Create your models here.
from django.core.validators import MaxValueValidator, MinValueValidator

current_academic_year = 2080


class Teacher(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)


class Class_name(models.Model):
    name = models.CharField(max_length=20)


class Student(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)


class Academic_Year(models.Model):
    year = models.IntegerField()


class Student_Information(models.Model):
    CASTE_CHOICES = [
        ('janajati', 'Janajati'),
        ('dalit', 'Dalit'),
        ('brahmin_chhetri', 'Brahmin/Chhetri'),
        ('others', 'Others'),
    ]

    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    school_id = models.CharField(max_length=20)
    year = models.PositiveIntegerField(
        validators=[MinValueValidator(2000), MaxValueValidator(9999)], null=True, blank=True)
    reg_id = models.CharField(max_length=20)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, blank=True)
    father_name = models.CharField(max_length=100, null=True, blank=True)
    mother_name = models.CharField(max_length=100, null=True, blank=True)
    date_of_birth_bs = models.DateField(null=True, blank=True)
    date_of_birth_ad = models.DateField(null=True, blank=True)
    disability = models.BooleanField(default=False)
    caste = models.CharField(max_length=50, choices=CASTE_CHOICES)


class Student_Document(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    profile_photo = models.FileField(
        upload_to="profile_photo", null=True, blank=True)
    birth_certificate = models.FileField(
        upload_to="birth_certificate", null=True, blank=True)
    other_doc = models.FileField(
        upload_to="other_document", null=True, blank=True)
