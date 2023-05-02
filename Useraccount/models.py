from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.db import models
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField


import uuid
TYPE_OF_USER = (
    ('Admin','Admin'),
    ('Customer', 'Customer'),
    ('Property Dealer', 'Property Dealer'),
)


class User(AbstractUser):
    email = models.EmailField(('email address'), unique=True)
    type = models.CharField(max_length=20, choices=TYPE_OF_USER, default='Customer')
    fullname = models.CharField(max_length=100)
    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = []

    
