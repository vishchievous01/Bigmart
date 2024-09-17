from django.db import models


# Create your models here.

class BigmartDb(models.Model):
    C_name = models.CharField(max_length=100, null=True, blank=True)
    Descptn = models.CharField(max_length=250, null=True, )
    C_image = models.ImageField(upload_to="Category Images", null=True, blank=True)


class ProductDb(models.Model):
    Category = models.CharField(max_length=100, null=True, blank=True)
    P_name = models.CharField(max_length=100, null=True, blank=True)
    Price = models.IntegerField(null=True, blank=True)
    Description = models.TextField(max_length=250, null=True, blank=True)
    P_image = models.ImageField(upload_to="Product Images", null=True, blank=True)