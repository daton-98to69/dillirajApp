from django.db import models
from accounts.models import CustomUser
# Create your models here.


class User_medias(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)


class Staff(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    teachers_unique_id = models.CharField(blank=True, null=True, max_length=12)
    date_of_entry = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.user.firstname} {self.teachers_unique_id}'
