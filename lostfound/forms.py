from django import forms
from .models import ItemList
from django.forms import Select

class ItemlistForm(forms.ModelForm):
    class Meta:
        model =  ItemList
        fields = ['title', 'status', 'category', 'mobile', 'ownername', 'description', 'image']
        widgets = {
                'category': Select(
                    attrs={
                        'class': 'js-example-basic-single'
                    }
                ),
            }