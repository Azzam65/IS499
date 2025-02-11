from django.shortcuts import redirect, render
from .forms import LicensePlateListingForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView

def home(request):
    return render(request, 'landingpage.html')

def auction(request):
    return render(request, 'auction.html')

def forsale(request):
    return render(request, 'forsale.html')

def addlisting(request):
    if request.method == "POST":
        form = LicensePlateListingForm(request.POST)
        if form.is_valid(): # save form to dataabase
            form.save()
            return redirect('home')  # Redirect to homepage or listings page
    else:
        form = LicensePlateListingForm()
    return render(request, 'addlisting.html', {'form': form})

# sign up view
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log in after sign up
            messages.success(request, "Registration successful!")
            return redirect('home')  # Redirect to homepage or dashboard
    else:
        form = UserCreationForm()
    
    return render(request, 'signup.html', {'form': form})

# login view
class CustomLoginView(LoginView):
    template_name = 'login.html'

class CustomLogoutView(LogoutView):
    next_page = 'home'  # Redirect after logout