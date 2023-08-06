from .models import ShippingAddress
from django import forms
from .models import ReviewRating


class ReviewForm(forms.ModelForm):
    class Meta:
        model = ReviewRating
        fields = ['subject', 'review', 'rating']


class ShippingAddressForm(forms.ModelForm):
    class Meta:
        model = ShippingAddress
        # Add any other fields you want to include in the form
        fields = ['address', 'city', 'country']
