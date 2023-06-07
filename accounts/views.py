# Create your views here.
from django.shortcuts import render, redirect
from .forms import RegistrationForm


def register(request):
    if request.method == 'POST':  # When the form is filled and submitted
        form = RegistrationForm(request.POST)     # Take the data from the form
        if form.is_valid():         # Check if the form is valid
            user = form.save()
            # Perform any additional actions, such as sending a confirmation email, etc.
            # Redirect to the desired page after successful registration
            return redirect('home')
    else:
        form = RegistrationForm()
        return render(request, 'registration/register.html', {'register-form': form})
