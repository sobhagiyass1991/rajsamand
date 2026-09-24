from django import forms
from django.http import request
from .models import BlogList
from django.core.exceptions import ValidationError
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required
from django.views import View
from django.forms import BaseModelFormSet
from django.db.models import Count, Sum
#from tinymce.widgets import TinyMCE
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

class BlogForm(forms.ModelForm):
        text = forms.CharField(widget=SummernoteWidget())  # instead of forms.Textarea
        class Meta:
            model = BlogList
            fields = ["title", "text"]
            #widgets = {'text': TinyMCE(attrs={'cols': 80, 'rows': 30})}
            widgets = {
            'text': SummernoteWidget(),
            }