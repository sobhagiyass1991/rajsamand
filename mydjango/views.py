from django.shortcuts import render
from .models import Blog, Author, Entry

# Create your views here.

def lists(request):
    blogs = Blog.objects.all()
    authors = Author.objects.all()
    entries = Entry.objects.all()
    context={
        'blogs' : blogs,
        'authors' : authors,
        'entries' : entries
    }
    return render(request, "mydjango.html", context)        
