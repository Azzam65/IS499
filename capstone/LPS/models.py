from django.db import models
from django.core.exceptions import ValidationError

class LicensePlateListing(models.Model):
    # Fields for the license plate
    numbers = models.CharField(max_length=4, verbose_name="Numbers")  # Max 4 digits
    letters = models.CharField(max_length=3, verbose_name="Letters")  # Max 3 letters

    # Listing type and pricing
    LISTING_TYPE_CHOICES = [
        ('buy_it_now', 'Buy It Now'),
        ('auction', 'Auction'),
    ]
    listing_type = models.CharField(
        max_length=12, 
        choices=LISTING_TYPE_CHOICES, 
        default='buy_it_now',
        verbose_name="Listing Type"
    )
    price = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        null=True, 
        blank=True, 
        verbose_name="Buy It Now Price"
    )
    starting_price = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        null=True, 
        blank=True, 
        verbose_name="Auction Starting Price"
    )

    # Timestamp
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")

    def __str__(self):
        return f"{self.numbers} {self.letters} - {self.get_listing_type_display()}"

    def clean(self):
        """
        Custom validation to ensure only one type of price is set.
        """
        super().clean()
        if self.listing_type == 'buy_it_now' and not self.price:
            raise ValidationError({'price': "Buy It Now price is required for this type."})
        if self.listing_type == 'auction' and not self.starting_price:
            raise ValidationError({'starting_price': "Starting price is required for auctions."})

    def save(self, *args, **kwargs):
        # Enforce validation before saving
        self.full_clean()
        super().save(*args, **kwargs)
