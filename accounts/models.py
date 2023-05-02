from django.db import models
from dashboard.models import *

class Contact_us(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phonenumber = models.CharField(max_length=15)
    message = models.TextField()
    
    def __str__(self):
        return str(self.name)
    
    
class ProjectReviews(models.Model):
    project_name = models.ForeignKey(
        Projects, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=500, null=True, blank=True)
    email = models.EmailField(max_length=500, null=True, blank=True)
    reviews = models.TextField()
    rating = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=500, choices=REVIEWS_CHOICES)


    def __str__(self):
        return self.project_name
    
    
class PropertiesReviews(models.Model):
    property_name = models.ForeignKey(
        Properties, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=500, null=True, blank=True)
    email = models.EmailField(max_length=500, null=True, blank=True)
    reviews = models.TextField()
    rating = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=500, choices=REVIEWS_CHOICES)


    def __str__(self):
        return self.property_name
