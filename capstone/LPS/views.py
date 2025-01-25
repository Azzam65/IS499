from django.shortcuts import redirect, render
from .forms import LicensePlateListingForm

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