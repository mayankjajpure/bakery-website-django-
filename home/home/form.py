from django import forms
from home.models import order

class form(forms.ModelForm):
    class Meta:
        method=order
        fields="__all__"