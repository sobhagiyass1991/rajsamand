from django.db.models import F
from random import randrange
from django.core.exceptions import ValidationError
from django.db import models
# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length = 100)

     
class Product(models.Model):
    title = models.CharField(max_length = 100)
    status = models.BooleanField()
    randomid = models.BigIntegerField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def save(self, **kwargs):
        self.randomid = randrange(1,3)
        if Product.objects.filter(randomid=self.randomid).exists():
           raise ValidationError("Not ok")
        super().save(**kwargs)


class Sample(models.Model):
    #auto = models.AutoField() // disabled for a model cant have more than one AutoField.
    #bigauto = models.BigAutoField(primary_key= True) // it cant be used as already a primary key is used.
    biginteger = models.BigIntegerField()
    binary = models.BinaryField()
    boolean = models.BooleanField()
    #pk = models.CompositePrimaryKey("decimal", "integer")
    char = models.CharField()
    date = models.DateField()
    decimal = models.DecimalField(max_digits=5, decimal_places = 2)
    duration = models.DurationField()
    email = models.EmailField()
    file = models.FileField(upload_to = "uploads/")
    file_path = models.FilePathField(path = "F:/srijan/bids")
    float = models.FloatField()
    generated_field = models.GeneratedField(
        expression = F("decimal") * F("float"),
        output_field = models.FloatField(),
        db_persist = True,
    )
    generic_ip_address = models.GenericIPAddressField()
    image = models.ImageField()
    integer = models.IntegerField()
    json = models.JSONField()
