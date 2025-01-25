from django.shortcuts import render

def home(request):
    return render(request, 'landingpage.html')

def auction(request):
    return render(request, 'auction.html')

def forsale(request):
    return render(request, 'forsale.html')
