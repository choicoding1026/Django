from django.db import models

# Create your models here.
class Product(models.Model):
    code = models.CharField(max_length=64, primary_key=True)
    name = models.CharField(max_length=64)
    price = models.IntegerField()
    pub_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table="product"