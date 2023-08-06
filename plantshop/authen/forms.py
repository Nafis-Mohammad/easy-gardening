from django import forms
from .models import UserProfile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['avatar', 'bio', 'address', 'phone_number']

        labels = {
            'avatar': 'Avatar',
            'bio': 'Bio',
            'address': 'Address',
            'phone_number': 'Phone Number',
        }

        widgets = {
            'avatar': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'bio': forms.Textarea(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }