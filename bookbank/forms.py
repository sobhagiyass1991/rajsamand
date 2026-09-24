from django import forms
from django.http import request
from .models import Category, BookBankList, BookIssueReturn
from django.core.exceptions import ValidationError
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required
from django.views import View
from django.forms import BaseModelFormSet
from django.db.models import Count, Sum
#from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

class BookBankForm(forms.ModelForm):
                #text = forms.CharField(widget=SummernoteWidget())  # instead of forms.Textarea
      class Meta:
           model = BookBankList
           fields = ["title", "author", "isbn", "publisher", "category", "status"]
            #widgets = {'text': SummernoteWidget(),}


class BookStatusForm(forms.ModelForm):
                #text = forms.CharField(widget=SummernoteWidget())  # instead of forms.Textarea
       class Meta:
           model = BookIssueReturn
           fields = ["takenby", "book", "bookstatus", "issuedate", "returndate"]
            #widgets = {'text': SummernoteWidget(),}
