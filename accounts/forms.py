from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm


class LoginForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)


class RegistrationForm(UserCreationForm):
    firstname = forms.CharField(max_length=30)
    lastname = forms.CharField(max_length=30)
    email = forms.EmailField(required=False)
    phonenumber = forms.CharField(max_length=15, required=False)
    school_unique_id = forms.CharField(max_length=50)
    date_of_birth = forms.DateTimeField(required=False)
    role = forms.ChoiceField(choices=CustomUser.ROLE_CHOICES)

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + \
            ('firstname', 'lastname', 'email',
             'phonenumber', 'school_unique_id', 'date_of_birth', 'role', 'username')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.firstname = self.cleaned_data['firstname']
        user.lastname = self.cleaned_data['lastname']
        user.email = self.cleaned_data['email']
        user.phonenumber = self.cleaned_data['phonenumber']
        user.school_unique_id = self.cleaned_data['school_unique_id']
        user.date_of_birth = self.cleaned_data['date_of_birth']
        user.role = self.cleaned_data['role']
        if commit:
            user.save()
        return user
