from django import forms
from django.http import request
from .models import Donor, Donation, Requestt
from django.core.exceptions import ValidationError
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required
from django.views import View
from django.forms import BaseModelFormSet
from django.db.models import Count, Sum

class SimpleForm(forms.ModelForm):
    name  = forms.CharField(max_length=100)
    address = forms.CharField(max_length=100)
    contact = forms.CharField(max_length=15)
    email = forms.EmailField()
    blood_group = forms.ChoiceField(
    choices=[
        ("A+", "A+"),
        ("A-", "A-"),
        ("B+", "B+"),
        ("B-", "B-"),
        ("O+", "O+"),
        ("O-", "O-"),
        ("AB+", "AB+"),
        ("AB-", "AB-"),
    ])
    status = forms.ChoiceField(
        choices = [
            ("0", "Available"),
            ("1", "Not Available"),
        ]
    )
    def clean_name(self):
        name = self.cleaned_data["name"]
        if "bharat" in name:
            raise ValidationError("Name cannot contain 'bharat'")
        return name
    
    class Meta:
        model = Donor
        fields = ["name", "address", "contact", "email", "blood_group", "status"]

class DonationForm(forms.ModelForm):
    #reve = reverse("blood:getbloodgroup", query = {"donorname": "donorname"} )
    #donorname = forms.ModelMultipleChoiceField(queryset=Donor.objects.all())
    #donorname = forms.ModelChoiceField(queryset=Donor.objects.all(), widget = forms.Select(attrs = {

    donorname = forms.ModelChoiceField(queryset=Donor.objects.all(), widget = forms.Select(attrs = {
        "hx-get" : reverse_lazy('blood:getbloodgroup'),
        "hx-target" : "#id_blood_group",
        "hx-trigger" : "change",
        "hx-swap" : "outerHTML",
        "hx-indicator" : "#spinner"

    }) )
    print(f" here is ths qs {donorname}")
    print(f" here is ths qs {donorname.queryset}")
    #blood_group  = forms.ModelChoiceField(queryset=Donor.objects.all(), widget=forms.Select(attrs={"id": "id_blood_group"}))
    #blood_group  = forms.CharField(required=False, widget=forms.TextInput(attrs={"id": "id_blood_group"}))
    #print(f"here is the blood grp {blood_group}")
    volume = forms.FloatField(required=True, widget=forms.NumberInput(attrs={}))

    class Meta:
        model = Donation
        fields = ["donorname", "blood_group",  "volume", "status"]
        #exclude = ["blood_group"]


class RequesttForm(forms.ModelForm):
    blood_group = forms.ChoiceField(
    choices=[
        ("A+", "A+"),
        ("A-", "A-"),
        ("B+", "B+"),
        ("B-", "B-"),
        ("O+", "O+"),
        ("O-", "O-"),
        ("AB+", "AB+"),
        ("AB-", "AB-"),
    ], widget= forms.Select(attrs={
        "hx-get" : reverse_lazy('blood:getbloodgroupvolume'),
        "hx-target" : "#getvolume",
        "hx-trigger" : "change",
        "hx-swap" : "innerHTML",
        "hx-indicator" : "#spinner"

    }

    ))

    def clean(self):
        cleaned_data  =   super().clean()
        print(f"here is cleaned data {cleaned_data}")
        volume = cleaned_data.get("volume")
        print(volume)
        blood_group =  cleaned_data.get("blood_group")
        print(blood_group)
        getdata  = Donation.objects.filter(blood_group__contains=blood_group).aggregate(Sum("volume"))
        print(getdata)
        if getdata["volume__sum"] <= volume:
            raise ValidationError("Not enough blood")

    class Meta:
        model = Requestt
        fields = ["patientname", "blood_group",  "doctorname", "volume"]

