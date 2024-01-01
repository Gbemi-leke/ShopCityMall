from django import forms
from frontend.models import *
from users.models import *
from django.core import validators
from django.db.migrations.state import get_related_models_tuples
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.forms import(PasswordResetForm, SetPasswordForm, UserChangeForm, UserCreationForm)


class SubscribeForm(forms.ModelForm):
    email = forms.EmailField(label='', widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'Email'}))
    class Meta:
        model = SubscribeModel
        fields = ['email']

class ContactForm(forms.ModelForm):
    first_name = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Name'}))
    email = forms.EmailField(label='Email :',
                             widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'E-mail'}))
    subject = forms.CharField(label='Subject :', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Subject'}))
    
    message = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Message',
        'id': 'message',
        'rows': '10',
        'cols':'30'
    }))
    
    class Meta():
     model = Contact
     fields = ['first_name', 'email', 'subject', 'message']

class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(label='Old Password', widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Old Password'}))
    new_password1 = forms.CharField(label='New Password', widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'New Password'}))
    new_password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Confirm Password'}))
    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])

class PasswordReset(PasswordResetForm):
    email = forms.EmailField(label='', widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email',}))
    
class SetPassword(SetPasswordForm):
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control form-control-lg', 'placeholder':'New Password'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control form-control-lg', 'placeholder':'Confirm Password'}))

class BlogForm(forms.ModelForm):

    class Meta():
        model = Blog
        fields = ['blog_img', 'blog_title','blog_description',]
        exclude = ['blog_date', 'user']

        widgets = { 
            'blog_img': forms.FileInput(attrs={'class': 'form-control'}),
            'blog_title': forms.TextInput(attrs={'class': 'form-control', 'type':'text', 'id':'floatingInput','placeholder': 'News'}),
            'blog_description': forms.Textarea(attrs={'class': 'form-control', 'id':'exampleFormControlTextarea1','rows':'6'}),     
        }

class EditBlogForm(forms.ModelForm):

    class Meta():
        model = Blog
        fields = ['blog_img', 'blog_title','blog_description',]
        exclude = ['blog_date', 'user']

        widgets = { 
            'blog_img': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'blog_title': forms.TextInput(attrs={'class': 'form-control', 'type':'text', 'id':'floatingInput','placeholder': 'News'}),
            'blog_description': forms.Textarea(attrs={'class': 'form-control', 'id':'exampleFormControlTextarea1','rows':'6'}),
        }


class FashionForm(forms.ModelForm):

    class Meta():
        model = Fashion
        fields = ['img1','img2','img3','img4', 'vendor_brand','product_detail','available_product','price','size','delivery_fee']
        exclude = ['date', 'user']

        widgets = { 
            'img1': forms.FileInput(attrs={'class': 'form-control'}),
            'img2': forms.FileInput(attrs={'class': 'form-control'}),
            'img3': forms.FileInput(attrs={'class': 'form-control'}),
            'img4': forms.FileInput(attrs={'class': 'form-control'}),
            'vendor_brand': forms.TextInput(attrs={'class': 'form-control', 'type':'text', 'id':'floatingInput','placeholder': 'BRAND'}),
            'price': forms.TextInput(attrs={'class': 'form-control', 'type':'text', 'id':'floatingInput','placeholder': 'Price'}),
            'available_product': forms.TextInput(attrs={'class': 'form-control', 'type':'text', 'id':'floatingInput'}),
            'size': forms.TextInput(attrs={'class': 'form-control', 'type':'text', 'id':'floatingInput'}),
            'delivery_fee': forms.TextInput(attrs={'class': 'form-control', 'type':'text', 'id':'floatingInput'}),
            'product_detail': forms.Textarea(attrs={'class': 'form-control', 'id':'exampleFormControlTextarea1','rows':'6'}),     
        }

class EditWearsForm(forms.ModelForm):

    class Meta():
        model = Fashion
        fields = ['img1','img2','img3','img4', 'vendor_brand','product_detail','available_product','price','size','delivery_fee']
        exclude = ['date', 'user']

        widgets = { 
            'img1': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'img2': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'img3': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'img4': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'vendor_brand': forms.TextInput(attrs={'class': 'form-control', 'type':'text', 'id':'floatingInput','placeholder': 'BRAND'}),
            'price': forms.TextInput(attrs={'class': 'form-control', 'type':'text', 'id':'floatingInput','placeholder': 'Price'}),
            'available_product': forms.TextInput(attrs={'class': 'form-control', 'type':'text', 'id':'floatingInput'}),
            'size': forms.TextInput(attrs={'class': 'form-control', 'type':'text', 'id':'floatingInput'}),
            'delivery_fee': forms.TextInput(attrs={'class': 'form-control', 'type':'text', 'id':'floatingInput'}),
            'product_detail': forms.Textarea(attrs={'class': 'form-control', 'id':'exampleFormControlTextarea1','rows':'6'}),     
        }


class PastriesForm(forms.ModelForm):

    class Meta():
        model = Pastries
        fields = ['image', 'vendor_brand','detail','price','delivery_fee']
        exclude = ['date', 'user']

        widgets = { 
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'vendor_brand': forms.TextInput(attrs={'class': 'form-control', 'type':'text', 'id':'floatingInput','placeholder': 'BRAND'}),
            'price': forms.TextInput(attrs={'class': 'form-control', 'type':'text', 'id':'floatingInput','placeholder': 'Price'}),
            'delivery_fee': forms.TextInput(attrs={'class': 'form-control', 'type':'text', 'id':'floatingInput'}),
            'detail': forms.Textarea(attrs={'class': 'form-control', 'id':'exampleFormControlTextarea1','rows':'6'}),     
        }

class EditPastriesForm(forms.ModelForm):

    class Meta():
        model = Pastries
        fields = ['image', 'vendor_brand','detail','price','delivery_fee']
        exclude = ['date', 'user']

        widgets = { 
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'vendor_brand': forms.TextInput(attrs={'class': 'form-control', 'type':'text', 'id':'floatingInput','placeholder': 'BRAND'}),
            'price': forms.TextInput(attrs={'class': 'form-control', 'type':'text', 'id':'floatingInput','placeholder': 'Price'}),
            'delivery_fee': forms.TextInput(attrs={'class': 'form-control', 'type':'text', 'id':'floatingInput'}),
            'detail': forms.Textarea(attrs={'class': 'form-control', 'id':'exampleFormControlTextarea1','rows':'6'}),     
        }


class GadgetsForm(forms.ModelForm):

    class Meta():
        model = Gadgets
        fields = ['img1','img2', 'vendor_brand','detail','available_product','price','delivery_fee','colour']
        exclude = ['date', 'user']

        widgets = { 
            'img1': forms.FileInput(attrs={'class': 'form-control'}),
            'img2': forms.FileInput(attrs={'class': 'form-control'}),
            'vendor_brand': forms.TextInput(attrs={'class': 'form-control', 'type':'text', 'id':'floatingInput','placeholder': 'BRAND'}),
            'price': forms.TextInput(attrs={'class': 'form-control', 'type':'text', 'id':'floatingInput','placeholder': 'Price'}),
            'colour': forms.TextInput(attrs={'class': 'form-control', 'type':'text', 'id':'floatingInput','placeholder': 'Colour'}),
            'available_product': forms.TextInput(attrs={'class': 'form-control', 'type':'text', 'id':'floatingInput'}),
            'delivery_fee': forms.TextInput(attrs={'class': 'form-control', 'type':'text', 'id':'floatingInput'}),
            'detail': forms.Textarea(attrs={'class': 'form-control', 'id':'exampleFormControlTextarea1','rows':'6'}),     
        }

class EditGadgetsForm(forms.ModelForm):

    class Meta():
        model = Gadgets
        fields = ['img1','img2', 'vendor_brand','detail','available_product','price','delivery_fee','colour']
        exclude = ['date', 'user']

        widgets = { 
            'img1': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'img2': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'vendor_brand': forms.TextInput(attrs={'class': 'form-control', 'type':'text', 'id':'floatingInput','placeholder': 'BRAND'}),
            'price': forms.TextInput(attrs={'class': 'form-control', 'type':'text', 'id':'floatingInput','placeholder': 'Price'}),
            'colour': forms.TextInput(attrs={'class': 'form-control', 'type':'text', 'id':'floatingInput','placeholder': 'Colour'}),
            'available_product': forms.TextInput(attrs={'class': 'form-control', 'type':'text', 'id':'floatingInput'}),
            'delivery_fee': forms.TextInput(attrs={'class': 'form-control', 'type':'text', 'id':'floatingInput'}),
            'detail': forms.Textarea(attrs={'class': 'form-control', 'id':'exampleFormControlTextarea1','rows':'6'}),     
        }
