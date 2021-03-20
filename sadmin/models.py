from django.db import models
from django.contrib.auth.models import User


# Employee Model

class Employee_Profile(models.Model):
    status      =   (
        ('active', 'active'),
        ('pending','pending'),
        ('rejected','rejected')
    )
    user        =   models.ForeignKey(User, on_delete = models.DO_NOTHING)
    name        =   models.CharField(max_length=100, blank=False)
    email       =   models.EmailField(null=True, blank=True)
    address     =   models.TextField(max_length=300, blank=True)
    contact     =   models.CharField(max_length=11, blank=False)
    status      =   models.CharField(max_length=8,choices=status)
    is_deleted  =   models.BooleanField(default=False)
    created_at  =   models.DateTimeField(auto_now_add=True)
    updated_at  =   models.DateTimeField(auto_now=True)
    
    class Meta:     
        verbose_name_plural = 'Employee Profiles'

    def __str__(self):
        return self.name 


class Degree(models.Model):
    name        =   models.CharField(max_length=200, blank=False)

    def __str__(self):
        return self.name


# doctor profile model 

class Doctor_Profile(models.Model):
    user        =   models.ForeignKey(User, on_delete=models.DO_NOTHING)
    name        =   models.CharField(max_length=200, blank=False)
    email       =   models.EmailField(null=True,blank=True)
    address     =   models.TextField(max_length=300, blank=True)
    degree      =   models.ManyToManyField(Degree, related_name='degree')
    contact     =   models.CharField(max_length=11,blank=False)
    created_at  =   models.DateTimeField(auto_now_add=True)
    updated_at  =   models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural =  "Doctor`s Profile"
        
    def __str__(self):
        return self.name 
    




