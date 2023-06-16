# Create your views here.
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegistrationForm
from .forms import LoginForm
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    context = {
        'user': request.user
    }
    return render(request, "accounts/home.html", context)


def login_view(request):  # Need to redirect to home page.
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Replace 'home' with the URL name of your home page
                if user.role == "admin":
                    return redirect("administration:admin_dashboard")
                elif user.role == "student":
                    return redirect("administration:admin_dashboard")
                else:
                    return HttpResponse(f"Is other: Loggedin, {user.lastname},{user.role}")
            else:
                form.add_error(None, 'Invalid username or password.')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})


def register(request):
    if request.method == 'POST':  # When the form is filled and submitted
        # Take the data from the form
        form = RegistrationForm(request.POST)
        if form.is_valid():         # Check if the form is valid
            form.save()
            # Perform any additional actions, such as sending a confirmation email, etc.
            # Redirect to the desired page after successful registration
            return HttpResponse("User Created")
    else:
        form = RegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})
