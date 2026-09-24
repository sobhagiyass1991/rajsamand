from django.db import models
from django.conf import settings 

class Category(models.Model):
    name = models.CharField(max_length = 100,null=True,blank=True)
    status = models.BooleanField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
            return f"{self.name}"

class BookBankList(models.Model):
    title=models.CharField(max_length = 100,null=True,blank=True)
    author=models.CharField(max_length = 100,null=True,blank=True)
    isbn=models.CharField(max_length = 101,null=True,blank=True)
    publisher=models.CharField(max_length = 102,null=True,blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    status = models.BooleanField()
    created_by  = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.title}"

class BookIssueReturn(models.Model):
    BOOK_STATUS = [
    ("Issued", "Issued"),
    ("Returned", "Returned"),
    ]
    takenby  = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="takenby")
    book = models.ForeignKey(BookBankList, on_delete=models.CASCADE, related_name="book")
    bookstatus = models.CharField(max_length=10, choices=BOOK_STATUS, default="Issued")
    issuedate = models.DateTimeField(blank=True, null=True)
    returndate = models.DateTimeField(blank=True, null=True)
    status = models.BooleanField(default=True)
    created_by  = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.book} {self.takenby} {self.bookstatus}"        