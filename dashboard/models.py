from django.db import models
from django_countries.fields import CountryField
from Useraccount.models import User


TYPE_CHOICES = [
    ('Rent', 'Rent'),
    ('Sale', 'Sale'),
]

CURRENCY_CHOICES = [
    ('INR', 'INR'),
    ('USD', 'USD'),
]

MODERATION_STATUS_CHOICES = [
    ('APPROVED', 'APPROVED'),
    ('PENDING', 'PENDING'),
    ('REJECTED', 'REJECTED'),
]

FACILITY_CHOICES = [
    ('HOSPITAL', 'HOSPITAL'),
    ('SUPERMARKET', 'SUPERMARKET'),
    ('SCHOOL', 'SCHOOL'),
    ('ENTERTAINMENT', 'ENTERTAINMENT'),
    ('PHARMACY', 'PHARMACY'),
    ('AIRPORT', 'AIRPORT'),
    ('RAILWAYS', 'RAILWAYS'),
    ('BUS STOP', 'BUS STOP'),
    ('BEACH', 'BEACH'),
    ('MALL', 'MALL'),
    ('BANK', 'BANK'),
    ('FITNESS', 'FITNESS'),
]

STATUS_CHOICES = [
    ('NOT AVAILABLE', 'NOT AVAILABLE'),
    ('PREPARING SELLING', 'PREPARING SELLING'),
    ('SELLING', 'SELLING'),
    ('SOLD', 'SOLD'),
    ('RENTING', 'RENTING'),
    ('RENTED', 'RENTED'),
    ('BUILDING', 'BUILDING'),

]
FACILITIES_CHOICE = [
    ('PUBLISHED', 'PUBLISHED'),
    ('DRAFT', 'DRAFT'),
    ('PENDING', 'PENDING'),
]
CATEGORIES_CHOICES = [
    ('VILLA', 'VILLA'),
    ('CONDO', 'CONDO'),
    ('Apartment', 'Apartment'),
    ('HOUSE', 'HOUSE'),
    ('LAND', 'LAND'),
    ('COMMERCIAL PROPERTY', 'COMMERCIAL PROPERTY'),
]
FAQCATEGORIES_CHOICES = [
    ('GENERAL', 'GENERAL'),
    ('BUYING', 'BUYING'),
    ('PAYING', 'PAYING'),
    ('SUPPORT', 'SUPPORT'),
]

REVIEWS_CHOICES = [
    ('APPROVED', 'APPROVED'),
    ('REJECTED', 'REJECTED'),
]
CATEGORY_CHOICES = [
    ('DESIGN', 'DESIGN'),
    ('DESIGN', 'DESIGN'),
]

RATING_CHOICES = [
        ('', '---------'),
        ('1', '★'),
        ('2', '★★'),
        ('3', '★★★'),
        ('4', '★★★★'),
        ('5', '★★★★★'),
]


class Facilities(models.Model):
    facility = models.CharField(max_length=500, choices=FACILITY_CHOICES)
    distance = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return str(self.id)

class city(models.Model):
        city_name = models.CharField(max_length=50)
        
        def __str__(self):
            return str(self.city_name)


class Projects(models.Model):

    Name = models.CharField(max_length=500, blank=True, null=True)
    description = models.TextField(null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    image = models.FileField(
        upload_to='Images/Properties', null=True, blank=True)
    country = CountryField(blank_label='(select country)', null=True)
    state = models.CharField(max_length=500)
    # city = models.CharField(max_length=500)
    city=models.ForeignKey(city,on_delete=models.CASCADE,null=True)
    project_location = models.CharField(max_length=5000, null=True, blank=True)
    Latitude = models.CharField(max_length=500, null=True, blank=True)
    Longitude = models.CharField(max_length=500, null=True, blank=True)
    number_of_blocks = models.IntegerField(default=0, null=True, blank=True)
    number_of_floors = models.IntegerField(default=0, null=True, blank=True)
    number_of_flats = models.IntegerField(default=0, null=True, blank=True)
    low_price = models.FloatField(default=0, null=True, blank=True)
    max_price = models.FloatField(default=0, null=True, blank=True)
    currency = models.CharField(max_length=50, choices=CURRENCY_CHOICES)
    facility = models.ManyToManyField(Facilities)
    status = models.CharField(max_length=500, choices=STATUS_CHOICES)
    unique_id = models.CharField(max_length=500, null=True, blank=True)
    # categories
    apartment = models.BooleanField(default=False)
    villa = models.BooleanField(default=False)
    condo = models.BooleanField(default=False)
    house = models.BooleanField(default=False)
    land = models.BooleanField(default=False)
    commercial_property = models.BooleanField(default=False)

    investors = models.CharField(max_length=500, null=True, blank=True)
    finish_date = models.DateField(auto_now_add=False, blank=True, null=True)
    sell_date = models.DateField(auto_now_add=False, blank=True, null=True)
    # Features
    wifi = models.BooleanField(default=False)
    parking = models.BooleanField(default=False)
    swimming_pool = models.BooleanField(default=False)
    balcony = models.BooleanField(default=False)
    garden = models.BooleanField(default=False)
    security = models.BooleanField(default=False)
    fitness_center = models.BooleanField(default=False)
    air_conditioning = models.BooleanField(default=False)
    central_heating = models.BooleanField(default=False)
    laundary_room = models.BooleanField(default=False)
    pets = models.BooleanField(default=False)
    spa_massage = models.BooleanField(default=False)
    created_at = models.DateTimeField(
        auto_created=True, auto_now_add=True, null=True)


    def __str__(self):
        return str(self.Name)


class Properties(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user_property', null=True)
    Title = models.CharField(max_length=500, blank=True, null=True)
    Type = models.CharField(max_length=500, choices=TYPE_CHOICES)
    description = models.TextField(null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    image = models.FileField(
        upload_to='Images/Properties', null=True, blank=True)
    country = CountryField(blank_label='(select country)', null=True)
    state = models.CharField(max_length=500)
    # city = models.CharField(max_length=500)
    city=models.ForeignKey(city,on_delete=models.CASCADE,null=True)
    property_location = models.CharField(
        max_length=5000, null=True, blank=True)
    Latitude = models.CharField(max_length=500, null=True, blank=True)
    Longitude = models.CharField(max_length=500, null=True, blank=True)
    number_of_bedrooms = models.IntegerField(default=0, null=True, blank=True)
    number_of_bathrooms = models.IntegerField(default=0, null=True, blank=True)
    number_of_floors = models.IntegerField(default=0, null=True, blank=True)
    square = models.IntegerField(default=0, null=True, blank=True)
    price = models.FloatField(default=0, null=True, blank=True)
    currency = models.CharField(max_length=50, choices=CURRENCY_CHOICES)
    facility = models.ManyToManyField(Facilities)
#     distance=models.ManyToManyField(Facilities)
    status = models.CharField(max_length=500, choices=STATUS_CHOICES)
    moderation_status = models.CharField(
        max_length=100, choices=MODERATION_STATUS_CHOICES)
    unique_id = models.CharField(max_length=500, null=True, blank=True)
    # categories
    apartment = models.BooleanField(default=False)
    villa = models.BooleanField(default=False)
    condo = models.BooleanField(default=False)
    house = models.BooleanField(default=False)
    land = models.BooleanField(default=False)
    commercial_property = models.BooleanField(default=False)
    project = models.ForeignKey(
        Projects, on_delete=models.CASCADE, related_name='project_name', null=True)
#     project=models.CharField(max_length=500,null=True,blank=True)
    account = models.CharField(max_length=500, null=True, blank=True)
    # Features
    wifi = models.BooleanField(default=False)
    parking = models.BooleanField(default=False)
    swimming_pool = models.BooleanField(default=False)
    balcony = models.BooleanField(default=False)
    garden = models.BooleanField(default=False)
    security = models.BooleanField(default=False)
    fitness_center = models.BooleanField(default=False)
    air_conditioning = models.BooleanField(default=False)
    central_heating = models.BooleanField(default=False)
    laundary_room = models.BooleanField(default=False)
    pets = models.BooleanField(default=False)
    spa_massage = models.BooleanField(default=False)
    created_at = models.DateTimeField(
        auto_created=True, auto_now_add=True, null=True)


    def __str__(self):
        return str(self.Title)


class Facility(models.Model):
    name = models.CharField(max_length=500, null=True, blank=True)
    icon = models.CharField(max_length=500, null=True, blank=True)
    status = models.CharField(max_length=500, choices=FACILITIES_CHOICE)
    created_at = models.DateTimeField(
        auto_created=True, auto_now_add=True, null=True)


    def __str__(self):
        return str(self.name)


class Investors(models.Model):
    name = models.CharField(max_length=500, null=True, blank=True)
    status = models.CharField(max_length=500, choices=FACILITIES_CHOICE)
    created_at = models.DateTimeField(
        auto_created=True, auto_now_add=True, null=True)


    def __str__(self):
        return str(self.name)


class Categories(models.Model):
    name = models.CharField(max_length=500, choices=CATEGORIES_CHOICES)
    parent = models.CharField(max_length=500, choices=CATEGORIES_CHOICES)
    description = models.TextField(null=True, blank=True)
    order = models.IntegerField(default=0, null=True, blank=True)
    status = models.CharField(max_length=500, choices=FACILITIES_CHOICE)
    created_at = models.DateTimeField(
        auto_created=True, auto_now_add=True, null=True)


    def __str__(self):
        return str(self.name)


class Features(models.Model):
    name = models.CharField(max_length=500, null=True, blank=True)
    icon = models.CharField(max_length=500, null=True, blank=True)
    created_at = models.DateTimeField(
        auto_created=True, auto_now_add=True, null=True)


    def __str__(self):
        return str(self.name)



class Testimonials(models.Model):
    name = models.CharField(max_length=500, null=True, blank=True)
    position = models.CharField(max_length=500, null=True, blank=True)
    content = models.TextField()
    status = models.CharField(max_length=500, choices=FACILITIES_CHOICE)
    image = models.FileField(
        upload_to='Images/Testimonials', null=True, blank=True)
    created_at = models.DateTimeField(auto_created=True, null=True)


    def __str__(self):
        return self.name


class Posts(models.Model):
    name = models.CharField(max_length=500, null=True, blank=True)
    description = models.TextField()
    content = models.TextField()
    created_at = models.DateField(
        auto_created=True, null=True, auto_now_add=True)
    status = models.CharField(
        max_length=500, choices=FACILITIES_CHOICE, null=True)
    categories = models.CharField(
        max_length=500, choices=CATEGORY_CHOICES, null=True)
    image = image = models.FileField(
        upload_to='Images/POSTS', null=True, blank=True)


    def __str__(self):
        return self.name


class BlogCategories(models.Model):
    name = models.CharField(max_length=500, null=True, blank=True)
    parent = models.CharField(max_length=500, choices=CATEGORIES_CHOICES)
    description = models.TextField(null=True, blank=True)
    order = models.IntegerField(default=0, null=True, blank=True)
    status = models.CharField(max_length=500, choices=FACILITIES_CHOICE)
    created_at = models.DateTimeField(auto_created=True, null=True)


    def __str__(self):
        return str(self.name)


class Tags(models.Model):
    name = models.CharField(max_length=500, null=True, blank=True)
    description = models.TextField()
    status = models.CharField(max_length=500, choices=FACILITIES_CHOICE)
    created_at = models.DateField(auto_created=True, null=True)


    def __str__(self):
        return str(self.name)


class FAQ(models.Model):
    category = models.CharField(max_length=100, choices=FAQCATEGORIES_CHOICES)
    questions = models.CharField(max_length=1000, null=True, blank=True)
    answer = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=100, choices=FACILITIES_CHOICE)
    created_at = models.DateTimeField(
        auto_created=True, auto_now_add=True, null=True)


    def __str__(self):
        return str(self.category)


# class Payments(models.Model):
#     payment_id = models.CharField(max_length=100)