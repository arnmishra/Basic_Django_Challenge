from django import forms
from django.contrib.auth.models import User
from finances.models import UserProfile

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    expense = forms.IntegerField(initial=0, help_text="Please enter your expense.")

    class Meta:
        model = UserProfile
        fields = ('expense', )
