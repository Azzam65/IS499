from django.shortcuts import render

# Create your views here.
def landingpage(request):
    return render(request, 'landingpage.html')

def profilepage(request):
    return render(request, 'profilepage.html')

def checkoutpage(request):
    return render(request, 'checkoutpage.html')

def searchingpage(request):
    return render(request, 'searchingpage.html')