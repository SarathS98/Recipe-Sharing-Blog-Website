from .models import Profile, Recipe
from django import forms
from django.contrib.auth.models import User

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'email')

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

class RecipesharingForm(forms.ModelForm):
    class Meta:
        
        model = Recipe
        fields = ['title','description']

        