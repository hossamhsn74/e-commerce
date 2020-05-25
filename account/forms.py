from django import forms
from django.contrib.auth.models import User
from .models import profile


class user_form(forms.ModelForm):
    username=forms.CharField(label=False,max_length=40,min_length=4,widget=forms.TextInput(attrs={
        'placeholder':'username',
        'required':True,
        'class':"input100",
    }))
    first_name=forms.CharField(label=False,widget=forms.TextInput(attrs={
        'placeholder':'first name',
        'class':"input100",

    }))
    last_name=forms.CharField(label=False,widget=forms.TextInput(attrs={
        'placeholder':'last name',
        'class':"input100",
    }))
    password=forms.CharField(label=False,min_length=5,max_length=30,widget=forms.PasswordInput(attrs={
        'placeholder':'password',
        'class':"input100",
    }))
    confirm_password=forms.CharField(label=False,min_length=5,max_length=30,widget=forms.PasswordInput(attrs={
        'placeholder':'confirm password',
        'class':"input100",
    }))

    email=forms.EmailField(label=False,widget=forms.EmailInput(attrs={
        'placeholder':'email',
        'class':"input100",
    }))

    class Meta:
        model=User
        fields=['username','first_name','last_name','password','email']

    
    def clean_username(self):
        username=self.cleaned_data.get('username')
        try:
            User.objects.get(username=username)
            raise forms.ValidationError("user name already exists")
        except User.DoesNotExist:
            return username

    def clean_email(self):
        email=self.cleaned_data.get('email')
        user=User.objects.filter(email=email)
        if user.exists():
            raise forms.ValidationError("email taken")
        return email

    def clean_confirm_password(self):
        password=self.cleaned_data.get('password')
        confirm_password=self.cleaned_data.get('confirm_password')
        if confirm_password != password:
            raise forms.ValidationError('password mismatch')
        return confirm_password

    


class profile_form(forms.ModelForm):
    phone_number=forms.CharField(label=False,max_length=11,min_length=3,widget=forms.TextInput(attrs={
        'placeholder':'Phone Number',
        'required':True,
        'class':"input100",
    }))
    image=forms.FileField(label=False,required=False)
    class Meta:
        model=profile
        fields=['phone_number','image']



class login_form(forms.Form):
    username=forms.CharField(label=False,widget=forms.TextInput(attrs={
        'placeholder':'username',
        'class':"input100",
    }))
    password=forms.CharField(label=False,widget=forms.PasswordInput(attrs={
        'placeholder':'password',
        'class':"input100",
    }))
    