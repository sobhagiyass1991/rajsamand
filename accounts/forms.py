import json
from django.shortcuts import render, get_object_or_404, redirect
from django import forms
from .models import Sample
from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django.conf import settings 
from django.contrib.auth import get_user_model
User = get_user_model()

class RegistrationForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class' : 'form-control' ,  'placeholder' : 'Enter Email Address'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control' ,  'placeholder' : 'Enter Email Address'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control' ,  'placeholder' : 'Enter Email Address'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control' ,  'placeholder' : 'Enter Email Address'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'form-control', 'placeholder' : 'Enter Password' }))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']



class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=150, 
        widget=forms.TextInput(attrs={'class' : 'form-control' , 'placeholder': 'Username'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class' : 'form-control' , 'placeholder': 'Password'})
    )

    class Meta:
        model = User
        fields = ['username', 'password']


class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control' ,  'placeholder' : 'Enter Email Address'}))
    middle_name = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control' ,  'placeholder' : 'Enter Email Address'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control' ,  'placeholder' : 'Enter Email Address'}))

    class Meta:
       model = User 
       #fields = ['gender']
       fields = ['first_name', 'middle_name', 'last_name']
       #fields = '__all__'


class SampleForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control' ,  'placeholder' : 'Enter Email Address'}))
    #middle_name = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control' ,  'placeholder' : 'Enter Email Address'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control' ,  'placeholder' : 'Enter Email Address'}))

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        if Sample.objects.get(first_name=first_name).exists():
            raise ValidationError("name already")
        return first_name
    
    class Meta:
        model = Sample
        fields= ['first_name', 'last_name']


class AdduserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email']        