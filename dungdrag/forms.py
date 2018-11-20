from django import forms

class SignUp(forms.Form):
    username = forms.CharField(max_length=100)
    email    = forms.EmailField()
    password = forms.CharField(max_length=100)

class Login(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)
