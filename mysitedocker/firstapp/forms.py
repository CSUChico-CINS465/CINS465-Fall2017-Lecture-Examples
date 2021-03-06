from django import forms
from django.core.validators import validate_unicode_slug

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import *

class suggestion_form(forms.Form):
    suggestion = forms.CharField(label='Suggestion', max_length=140, validators=[validate_unicode_slug])
    image=forms.ImageField(label="Image File")
    image_description=forms.CharField(label="Image Description", max_length=144)

    def save(self, request , commit=True):
        suggest = suggestion()
        suggest.suggestion=self.cleaned_data['suggestion']
        suggest.image=self.cleaned_data['image']
        suggest.idescription=self.cleaned_data['image_description']
        suggest.author=request.user
        if commit:
            suggest.save()
        return suggest
    # CHOICES = (('1', 'First',), ('2', 'Second',))
    # choice_field = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)

class comment_form(forms.Form):
    comment = forms.CharField(
        label='Comment',
        max_length=140,
        validators=[validate_unicode_slug],
        widget=forms.TextInput(
            attrs={'placeholder': 'Add a comment'}
        )
    )

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

class registration_form(UserCreationForm):
    email = forms.EmailField(
        label="Email",
        required=True
        )

    class Meta:
        model = User
        fields = ("username", "email",
            "password1", "password2")

    def save(self, commit=True):
        user=super(registration_form,self).save(commit=False)
        user.email=self.cleaned_data["email"]
        if commit:
            user.save()
        return user
