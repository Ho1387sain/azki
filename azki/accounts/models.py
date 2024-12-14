from django.db import models
from iranian_cities.fields import OstanField, ShahrestanField







class UserProfile(models.Model):
    username = models.CharField(max_length=20,null=True,blank=True)
    number = models.CharField(max_length=20,null=True, blank=True)
    password = models.CharField(max_length=12,null=True, blank=True)
    job = models.CharField(max_length=20,null=True, blank=True)
    Shahr = ShahrestanField(null=True, blank=True)
    Ostan = OstanField(null=True, blank=True)
    national_code = models.CharField(max_length=20,null=True, blank=True)
    email = models.EmailField( default='ali@gmail.com',null=False, blank=False)
    address = models.TextField(null=True, blank=True)
    
     
    # def __str__(self):
    #     return self.user


