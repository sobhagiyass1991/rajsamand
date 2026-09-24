from django import forms
from django.contrib.auth.models import User
from .models import ServiceProvider
from django.core.exceptions import ValidationError
from django.http import HttpResponse

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
