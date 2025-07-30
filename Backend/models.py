from django.db import models
from django.contrib.auth.models import User


# Create your models here.

# admin profile
class AdminProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='admin_images/', default='admin_images/default.png')

    def __str__(self):
        return self.user.username

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