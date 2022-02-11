from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class UserRegistrationForm(UserCreationForm):
    """ User registration """
    first_name = forms.CharField(
        max_length=30, required=False,
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'placeholder': 'first name',
                   'type': 'text',
                   'id': 'first_name'
                   }
        ))

    last_name = forms.CharField(
        max_length=30,
        required=False,
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Last name',
                   'type': 'text',
                   'id': 'last_name'
                   }
        ))

    email = forms.EmailField(
        max_length=254,
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'placeholder': 'email address',
                   'type': 'text',
                   'id': 'email_address'
                   }
        ))

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name",
                  "email", "password1", "password2")

    def clean_email(self):
        """Prevent existing email from registration"""
        email = self.cleaned_data["email"]
        if User.objects.filter(email=email).exists():
            raise ValidationError("A user with this email already exists!")
        return email


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email")


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('date_of_birth', 'photo')
