from django import forms
from django.forms import MultipleChoiceField, BooleanField, CheckboxInput, CheckboxSelectMultiple
from django.contrib.auth.models import User
from .models import PropertyList
from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django_summernote.widgets import SummernoteWidget

class PropertyForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            configs = self.instance.configs
            ptypes = self.instance.ptype
            print(ptypes)
            if configs:
            # DB में "['Park', 'Green']" जैसा string stored है
                import ast
                configs = ast.literal_eval(configs)

                self.initial["configs"] = configs

        if kwargs['instance'].status == True:
            self.fields["status"].widget.attrs.update({"checked": ""})
        else:
            self.fields["status"].widget.attrs.update({})

    PTYPES = [
        ("Apartment" , "Apartment"),
        ("Independent House" , "Independent House"),
        ("Independent Floor" , "Independent Floor"),
        ("Plot " , "Plot "),
        ("Studio" , "Studio"),
        ("Duplex" , "Duplex"),
        ("Penthouse" , "Penthouse"),
        ("Villa" , "Villa"),
        ("Agriculture Land" , "Agriculture Land"),
    ]

    FUR_TYPES = [
        ("Furnished" , "Furnished"),
        ("Semi-Furnished" , "Semi-Furnished"),
        ("Unfurnished" , "Unfurnished"),
    ]

    COLORS_CHOICES = [
    ("Park" , "Park"),
    ("Green" , "Green"),
    ("Black" , "Black"),
    ]
    title = forms.CharField(widget = forms.TextInput(attrs={"class": "form-control",}))
    ptype = forms.ChoiceField(choices=PTYPES, widget = forms.RadioSelect(attrs={"class": "form-check-input mt-0",}))
    configs = MultipleChoiceField(choices=COLORS_CHOICES, widget = forms.CheckboxSelectMultiple(attrs={"class": "form-check-input ms-0 mt-0", "type" : "checkbox"}))
    status = BooleanField(required=False, widget = forms.CheckboxInput(attrs={"class": "form-check-input ms-0 mt-0",}))
    class Meta:
        model = PropertyList
        fields = ['title', 'ptype', 'configs', 'status']
        #fields = ['title', 'ptype', 'area', 'price', 'image', 'features', 'status', 'details']
        #fields = "__all__"
        widgets = {
            'details': SummernoteWidget(),
        }
        

