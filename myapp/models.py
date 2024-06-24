from django.db import models

# Create your models here.
class servicedb(models.Model):
    Service = models.CharField(max_length=100, null=True, blank=True)
    Image = models.ImageField(upload_to="service", null=True, blank=True)

class employeedb(models.Model):
    Empname = models.CharField(max_length=100, null=True, blank=True)
    Mobile = models.IntegerField(null=True, blank=True)
    Email = models.EmailField(max_length=100, null=True, blank=True)
    Salary = models.IntegerField(null=True, blank=True)
    Image = models.ImageField(upload_to="employee", null=True, blank=True)
class gallerydb(models.Model):
    Title = models.CharField(max_length=100, null=True, blank=True)
    Image = models.ImageField(upload_to="gallery", null=True, blank=True)
class registerdb(models.Model):
    Username = models.CharField(max_length=50, null=True, blank=True)
    Email = models.EmailField(max_length=50, null=True, blank=True)
    Mobile = models.IntegerField(null=True, blank=True)
    Password = models.CharField(max_length=50, null=True, blank=True)
class workdb(models.Model):
    Date = models.DateField(auto_now=True)
    Customer = models.CharField(max_length=50, null=True, blank=True)
    Mobile = models.IntegerField(null=True, blank=True)
    Email = models.EmailField(max_length=50, null=True, blank=True)
    Content = models.CharField(max_length=50, null=True, blank=True)
    ContentImage = models.ImageField(upload_to="works", null=True, blank=True)
    Service = models.CharField(max_length=50, null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    status = models.CharField(max_length=50, default="Pending")
    Amount = models.FloatField(null=True, blank=True)

