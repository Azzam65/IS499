from django.shortcuts import render
from .models import UserTable

def landing_page(request):
    users = UserTable.objects.all()
    return render(request, 'landingpage.html', {'users': users})
    
def home(request):
    return render(request, 'landingpage.html')

def auction(request):
    return render(request, 'auction.html')

def forsale(request):
    return render(request, 'forsale.html')

