from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(UserCreationForm):
    # password = forms.CharField(widget=forms.PasswordInput)

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + \
            ('username', 'password', 'firstname', 'lastname', 'email',
             'phonenumber', 'school_unique_id', 'date_of_birth', 'role')


