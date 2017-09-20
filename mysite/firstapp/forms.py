from django import forms
from django.core.validators import validate_unicode_slug

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class suggestion_form(forms.Form):
    suggestion = forms.CharField(label='Suggestion', max_length=140, validators=[validate_unicode_slug])

class LoginForm(AuthenticationForm):
    username=forms.CharField(
        label="Username",
        max_length=30,
        widget=forms.TextInput(attrs={
            'name':'username'
        })
    )
    password=forms.CharField(
        label="Password",
        max_length=32,
        widget=forms.PasswordInput()
    )
