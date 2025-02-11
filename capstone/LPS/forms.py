from django import forms
from .models import LicensePlateListing

class LicensePlateListingForm(forms.ModelForm):
    LISTING_TYPE_CHOICES = [
        ('buy_it_now', 'Buy It Now'),
        ('auction', 'Auction'),
    ]

    # Add listing type as a radio button
    listing_type = forms.ChoiceField(
        choices=LISTING_TYPE_CHOICES,
        widget=forms.RadioSelect(attrs={'class': 'addlisting'}),
        label="Listing Type"
    )
    # Add a field for auction starting price
    starting_price = forms.DecimalField(
        required=False,  # Only required for auction
        max_digits=10,
        decimal_places=2,
        widget=forms.NumberInput(attrs={'placeholder': 'Enter starting price for auction', 'class': 'addlisting'}),
        label="Starting Price"
    )

    class Meta:
        model = LicensePlateListing
        fields = ['numbers', 'letters', 'price', 'listing_type', 'starting_price']
        widgets = {
            'numbers': forms.TextInput(attrs={'placeholder': 'Enter up to 4 numbers', 'maxlength': '4', 'class': 'addlisting'}),
            'letters': forms.TextInput(attrs={'placeholder': 'Enter exactly 3 letters', 'maxlength': '3', 'class': 'addlisting'}),
            'price': forms.NumberInput(attrs={'placeholder': 'Enter Buy It Now price', 'class': 'addlisting'}),
        }
        labels = {
            'numbers': 'Numbers',
            'letters': 'Letters',
            'price': 'Buy It Now Price',
        }

    def clean(self):
        cleaned_data = super().clean()
        listing_type = cleaned_data.get('listing_type')
        price = cleaned_data.get('price')
        starting_price = cleaned_data.get('starting_price')

        # Validate based on listing type
        if listing_type == 'buy_it_now' and not price:
            raise forms.ValidationError("Please provide a Buy It Now price.")
        if listing_type == 'auction' and not starting_price:
            raise forms.ValidationError("Please provide a starting price for the auction.")

        return cleaned_data
