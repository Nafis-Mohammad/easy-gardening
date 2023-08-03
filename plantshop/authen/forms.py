from django import forms
from .models import UserProfile
from django import forms
from django.forms import ModelForm
from plantapp.models import Wish


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


class WishForm(ModelForm):

    wishtitle = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    wish = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    link = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    is_achieved = forms.BooleanField(widget=forms.CheckboxInput(
        attrs={'class': 'form-check-input mt-0'}), required=False)
    image = forms.ImageField(widget=forms.FileInput(
        attrs={'class': 'form-control'}))

    class Meta:

        model = Wish
        fields = ('wishtitle', 'wish', 'link', 'is_achieved', 'image')

        labels = {
            'wishtitle': 'Wish Title',
            'wish': 'Wish',
            'link': 'Link',
            'is_achieved': 'Is Achieved',
            'image': 'Image'
        }
