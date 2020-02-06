from django import forms
from .models import customer

class my_form(forms.Form):
    first_name = forms.CharField(label='first name :', max_length=100)
    last_name = forms.CharField(label='last name :', max_length=100)
    email = forms.EmailField(label='email :')
    mobile = forms.IntegerField(label='mobile :')
    password = forms.CharField(label='password :')
