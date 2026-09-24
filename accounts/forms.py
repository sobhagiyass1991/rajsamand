import json
from django.shortcuts import render, get_object_or_404, redirect
from django import forms
from .models import Sample
#, Teacher, Subject, Jobslist, School, Student, SubjectMark
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

    def clean(self):
        cleaned_data = super().clean()
        un = cleaned_data.get('username')
        em = cleaned_data.get('email')
        if un == em:
            raise forms.ValidationError("Both cant be same ")

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

    GENDER = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Transgender', 'Transgender')
    ]
    
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control' ,  'placeholder' : 'Enter Email Address'}))
    middle_name = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control' ,  'placeholder' : 'Enter Email Address'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control' ,  'placeholder' : 'Enter Email Address'}))
    gender = forms.ChoiceField(choices=GENDER, widget=forms.Select(attrs={'class': 'form-control'}))
    mobile = forms.CharField(widget=forms.NumberInput(attrs={'class' : 'form-control' ,  'placeholder' : 'Enter Email Address'}))
    dob = forms.DateField(widget=forms.DateInput(attrs={"type" : "date", 'class' : 'form-control', "format " : "%Y-%m-%d"}))
    address = forms.CharField(widget=forms.Textarea(attrs={'class' : 'form-control' ,  'placeholder' : 'Enter Email Address'}))
    #role = forms.ChoiceField(choices=GENDER, widget=forms.Select(attrs={'class': 'form-control'}))
    
    def clean_mobile(self):
        mobile  = self.cleaned_data['mobile']
        if len(mobile)<10:
            raise forms.ValidationError("Lentg shoudl be low")
        elif User.objects.filter(mobile=mobile).exclude(id=self.instance.id).exists():
            raise forms.ValidationError("Moble already exists")
        else:
            pass
        return mobile
    
    class Meta:
       model = User 
       #fields = ['gender']
       fields = ['first_name', 'middle_name', 'last_name', 'gender', 'mobile', 'dob', 'address', 'role']
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


class UserRegistrationForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class' : 'form-control' ,  'placeholder' : 'Enter Email Address'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control' ,  'placeholder' : 'Enter Email Address'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control' ,  'placeholder' : 'Enter Email Address'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control' ,  'placeholder' : 'Enter Email Address'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'form-control', 'placeholder' : 'Enter Password' }))

    def clean(self):
        cleaned_data = super().clean()
        un = cleaned_data.get('username')
        em = cleaned_data.get('email')
        if un == em:
            raise forms.ValidationError("Both cant be same ")

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password', 'role']


