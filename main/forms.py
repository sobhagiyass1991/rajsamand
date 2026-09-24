import json
from django.shortcuts import render, get_object_or_404, redirect
from django import forms
from django.contrib.auth.models import User
from .models import Contact, Pincode 
from localservices.models import ServiceProvider
from django.core.exceptions import ValidationError
from django.http import HttpResponse

class RegistrationForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class' : 'form-control' ,  'placeholder' : 'Enter Email Address'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control' ,  'placeholder' : 'Enter Email Address'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control' ,  'placeholder' : 'Enter Email Address'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control' ,  'placeholder' : 'Enter Email Address'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'form-control', 'placeholder' : 'Enter Password' }))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']


class LoginForm(forms.ModelForm):
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


class ContactForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class' : 'input',
            'placeholder' : 'Contact Name'
        })
    )

    email = forms.CharField(
        widget=forms.EmailInput(attrs={
            'class' : 'input',
            'placeholder' : 'Contact Name'
        })
    )

    document = forms.FileField(
        widget=forms.FileInput(attrs={
            'class' : 'file-input file-input-bordered w-full',
            'placeholder' : 'Contact Name'
        }),
        required= False 
    )


    def clean_email(self):
        email = self.cleaned_data['email']
        if Contact.objects.filter(user=self.initial.get('user'), email=email).exists():
            raise ValidationError("You have already this email to system.")
        return email
    
    class Meta:
        model = Contact
        fields = ['name', 'email', 'document']


class ProfileForm(forms.ModelForm):
    class Meta:
        #model = SrijanProfile
        #fields = ['first_name', 'last_name' , 'email', 'middle_name']
        fields = "__all__" 
        exclude = ['user_id',]


        GENDER = [
            ("Male" , "Male"),
            ("Female" , "Female")
        ]
        widgets = {
            'user_id' : forms.TextInput(attrs={'class' : 'form-control', 'disabled' : 'disabled'}),
            'srijan_id' : forms.NumberInput(attrs={'class' : 'form-control', 'disabled' : 'disabled'}),
            'first_name' : forms.TextInput(attrs={'class' : 'form-control'}),
            'last_name' : forms.TextInput(attrs={'class' : 'form-control'}),
            'middle_name' : forms.TextInput(attrs={'class' : 'form-control'}),
            'dob' : forms.DateInput(attrs={'class' : 'form-control'}),
            'email' : forms.EmailInput(attrs={'class' : 'form-control'}),
            'username' : forms.TextInput(attrs={'class' : 'form-control'}),
            'mobile' : forms.NumberInput(attrs={'class' : 'form-control'}),
            'gender' : forms.Select(choices=GENDER, attrs={'class' : 'form-select'}),

        }

        '''
        def __init__(self, *args, **kwargs):
            page_fields = kwargs.pop('fields', None)

            super().__init__(*args, **kwargs)
        
            if page_fields: 
                #allowed = set(page_fields)
                #existing = set(self.fields.keys())
                for field in list(self.fields.keys()):
                    if field not in page_fields:
                        self.fields.pop(field)
                        '''
        


class PincodeForm(forms.ModelForm):
    office = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class' : 'form-control' , 'placeholder': 'Username'}))
    circle = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class' : 'form-control' , 'placeholder': 'Username'}))
    pincode = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class' : 'form-control' , 'placeholder': 'Username'}))

    def clean_pincode(self):
        pincode = self.cleaned_data["pincode"]
        if Pincode.objects.filter(pincode=pincode).exists():
            raise forms.ValidationError("यह पिनकोड पहले से है।") 
        return pincode 

    class Meta:
        model = Pincode
        fields = ['office', 'circle', 'pincode']

class ServiceForm(forms.ModelForm):
    name = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class' : 'form-control' , 'placeholder': 'Enter Business name'}))

    def clean_name(self):
        name = self.cleaned_data["name"]
        if ServiceProvider.objects.filter(name=name).exists():
            raise ValidationError("ohh name exists")
        return name
    
    class Meta:
        model = ServiceProvider
        fields = ['name', 'status', 'details', 'image', 'service']
        #fields = "__all__"
