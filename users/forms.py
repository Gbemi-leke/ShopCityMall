from django import forms
from users.models import *
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import UserCreationForm


class EditUserForm(forms.ModelForm):
    image = forms.ClearableFileInput(attrs={'class': 'form-control'})

    user_name = forms.CharField( widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder': 'Username' }))

    first_name = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': ' FirstName'}))

    last_name = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': ' lastName'}))
    
    phone_number = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': ' Phone No:'}))
    
    email = forms.EmailField(required=False, widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'Email'}))
    
    about = forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'About Yourself'})

    

    class Meta():
        model = NewUser
        fields = ['image', 'user_name', 'first_name', 'last_name', 'email', 'phone_number', 'about']
              

    def save(self, commit=True):
        user = super().save(commit=False)
        user.user_name = self.cleaned_data['user_name']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name'] 
        user.phone_number = self.cleaned_data['phone_number'] 
        user.email = self.cleaned_data['email']
        user.image = self.cleaned_data['image']
        user.about = self.cleaned_data['about']
    
        if commit:
            user.save()
            return user
        

class RegisterForm(UserCreationForm):
    IS_VENDOR = "V"
    IS_USER = "U"
    CHOOSE = ""

    ACCOUNT_TYPE = [
        (IS_VENDOR, 'Vendor'),
        (IS_USER, 'User'),
        (CHOOSE, 'Type of account')

    ]

    first_name = forms.CharField(required=False, widget=forms.TextInput(
        attrs={ 'placeholder': 'First name'}))
    user_name = forms.CharField(label='Username', widget=forms.TextInput(
        attrs={ 'placeholder': 'Username'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput
        (attrs={ 'placeholder': 'Email'}))
    password1 = forms.CharField(label='Enter Password', widget=forms.PasswordInput(
        attrs={ 'placeholder': 'Password'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(
        attrs={ 'placeholder': 'Confirm password'}))
    
    account_type = forms.CharField(required=False, label='Type of account:', widget=forms.Select(choices=ACCOUNT_TYPE,
        attrs={'class': 'form-control', 'placeholder': 'Type of account'}))

        
    def clean_email(self):
        email_field = self.cleaned_data.get('email')
        if NewUser.objects.filter(email=email_field).exists():
            raise forms.ValidationError('Email already exist')
        return email_field

    class Meta():
        model = NewUser
        fields = [ 'first_name','user_name', 'password1', 'password2','is_admin','account_type']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.user_name = self.cleaned_data['user_name']
        user.email = self.cleaned_data['email']
        user.account_type = self.cleaned_data['account_type']

        if commit:
            user.save()
            return user

