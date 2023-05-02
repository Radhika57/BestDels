
from django.contrib import admin
from .models import *
# Register your models here.
class CityAdmin(admin.ModelAdmin):
    list_display=['city_name']

class PropertyAdmin(admin.ModelAdmin):
    list_display=['Title','Type']

class FacilitiesAdmin(admin.ModelAdmin):
    list_display=['id','facility','distance']
    
class ProjectsAdmin(admin.ModelAdmin):
    list_display=['Name','description']

class FacilityAdmin(admin.ModelAdmin):
    list_display=['name','status']

class InvestorsAdmin(admin.ModelAdmin):
    list_display=['name','status']

class CategoriesAdmin(admin.ModelAdmin):
    list_display=['name','status']

class FeaturesAdmin(admin.ModelAdmin):
    list_display=['name']


class TestimonialsAdmin(admin.ModelAdmin):
    list_display=['name','image','position','content','status']
    
class FAQAdmin(admin.ModelAdmin):
    list_display = ['category','questions']


class PostsAdmin(admin.ModelAdmin):
    list_display=['name','description','content','created_at']

class BlogCategoriesAdmin(admin.ModelAdmin):
    list_display=['name','parent','description','status','created_at']

class TagsAdmin(admin.ModelAdmin):
    list_display=['name','description','status']
    
# class PaymentAdmin(admin.ModelAdmin):
#     list_display=['payment_id']

admin.site.register(Properties,PropertyAdmin)
admin.site.register(Facilities,FacilitiesAdmin)
admin.site.register(Investors,InvestorsAdmin)
admin.site.register(Projects,ProjectsAdmin)
admin.site.register(Facility,FacilityAdmin)
admin.site.register(Categories,CategoriesAdmin)
admin.site.register(Features,FeaturesAdmin)
admin.site.register(Testimonials,TestimonialsAdmin)
admin.site.register(FAQ,FAQAdmin)
admin.site.register(Posts,PostsAdmin)
admin.site.register(BlogCategories,BlogCategoriesAdmin)
admin.site.register(Tags,TagsAdmin)
admin.site.register(city,CityAdmin)
# admin.site.register(Payments,PaymentAdmin)
