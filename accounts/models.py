from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

# Groups can be created to specify various permission to different types of users.


class CustomUser(AbstractUser):
    ADMIN = 'admin'
    SUB_ADMIN = 'sub_admin'
    STUDENT = 'student'
    TEACHER = 'teacher'

    ROLE_CHOICES = (
        (ADMIN, 'Admin'),
        (SUB_ADMIN, 'Sub Admin'),
        (STUDENT, 'Student'),
        (TEACHER, 'Teacher'),
    )
    # Add custom fields
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    email = models.EmailField(unique=True, null=True, blank=True)
    phonenumber = models.CharField(max_length=15, null=True, blank=True)
    school_unique_id = models.CharField(max_length=50, unique=True)
    date_of_birth = models.DateTimeField(null=True, blank=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    # Additional fields specific to each role
    # Additional fields and methods

    def is_admin(self):
        return self.role == self.ADMIN

    def is_sub_admin(self):
        return self.role == self.SUB_ADMIN

    def is_student(self):
        return self.role == self.STUDENT

    def is_teacher(self):
        return self.role == self.TEACHER
