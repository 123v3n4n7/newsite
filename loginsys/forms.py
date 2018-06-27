from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Profile


class UserRegistrationForm(forms.ModelForm):
    usernmae = forms.CharField(label="username", max_length=100, min_length=5)
    email = forms.EmailField()
    password1 = forms.CharField(label="password", max_length=100, min_length=8, widget=forms.PasswordInput)
    password2 = forms.CharField(label="confirm password", max_length=100, min_length=8, widget=forms.PasswordInput)

    def clean_email(self):
        email = self.cleaned_data("email")
        qs = User.objects.filter(email)
        if qs.exist():
            raise ValidationError("email is alredy exist")
        return email


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'birth_date', 'age', 'places', 'music', 'hobby', 'picture']
