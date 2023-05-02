from django.contrib import admin
from .models import *

class ContactusAdmin(admin.ModelAdmin):
    list_display=['name','email','phonenumber','message']
    
class ProjectReviewsAdmin(admin.ModelAdmin):
    list_display=['name','rating'] 
 
class PropertyReviewsAdmin(admin.ModelAdmin):
    list_display=['name','rating']    
    
admin.site.register(ProjectReviews,ProjectReviewsAdmin)
admin.site.register(Contact_us,ContactusAdmin)
admin.site.register(PropertiesReviews,PropertyReviewsAdmin)


