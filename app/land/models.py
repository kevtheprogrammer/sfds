from django.db import models
from django.urls import reverse

from account.models import  User 

# Create your models here.
class SoilNutrient(models.Model):
    name = models.CharField(max_length = 150,default=None)
    description = models.TextField(default=None)
    client = models.ForeignKey(User, on_delete=models.CASCADE,related_name='client', default=None)    
    nitrogen = models.CharField(max_length=900)
    phosphorous = models.CharField(max_length=900)
    potasium = models.CharField(max_length=900)
    is_fertile = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,related_name='author', default=None)
    
    
    def __str__(self):
        return self.name


class RecommendedPlant(models.Model):
    imagev  = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    name = models.CharField(max_length=250)
    soil = models.ForeignKey(SoilNutrient, on_delete=models.CASCADE, related_name='soil')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
    def __str__(self):
        return self.document.name