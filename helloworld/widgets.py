from django import forms

class GreetingForm(forms.Form):
    name = forms.CharField(max_length=100)
