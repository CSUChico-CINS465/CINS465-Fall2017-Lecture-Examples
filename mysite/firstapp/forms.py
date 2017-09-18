from django import forms
from django.core.validators import validate_unicode_slug

class suggestion_form(forms.Form):
    suggestion = forms.CharField(label='Suggestion', max_length=140, validators=[validate_unicode_slug])
