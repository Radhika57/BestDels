from django import forms
from .models import *
from django.forms import modelformset_factory
from ckeditor.widgets import CKEditorWidget
from django.forms.widgets import Select
from crispy_forms.layout import Field
from django.utils.html import format_html

class CityForm(forms.ModelForm):
    class Meta:
        model = city
        fields = '__all__'

class PropertiesForm(forms.ModelForm):
    class Meta:
        model = Properties
        # fields = '__all__'
        exclude = ["facility","created_at","user"]       

        
class DealerPropertiesForm(forms.ModelForm):
    class Meta:
        model = Properties
        # fields = '__all__'
        exclude = ["facility","created_at","moderation_status","user"] 
 
class BirdForm(forms.ModelForm):
    class Meta:
        model = Facilities
        fields = ["facility","distance"]
        
BirdFormSet = modelformset_factory(Facilities, fields=("facility","distance",), extra=1)
        
class ProjectsForm(forms.ModelForm):
    class Meta:
        model = Projects
        # fields = '__all__'
        exclude = ["facility","created_at"] 
        
class FacilitiesForm(forms.ModelForm):
    class Meta:
        model=Facility
        # fields = '__all__'
        exclude = ["created_at"] 
        
class InvestorsForm(forms.ModelForm):
    class Meta:
        model=Investors
        exclude = ["created_at"] 
        # fields='__all__'


class CategoriesForm(forms.ModelForm):
    class Meta:
        model = Categories
        # fields = '__all__'
        exclude = ["created_at"] 

class FeaturesForm(forms.ModelForm):
    class Meta:
        model = Features
        # fields = '__all__'
        exclude = ["created_at"] 
        
class FAQForm(forms.ModelForm):
    class Meta:
        model = FAQ
        # fields = '__all__'
        exclude = ["created_at"] 


class TestimonialsForm(forms.ModelForm):
    class Meta:
        model = Testimonials
        # fields = '__all__'
        exclude = ["created_at"] 



class PostsForm(forms.ModelForm):
    class Meta:
        model=Posts
        exclude=['created_at']

class BlogCategoriesForm(forms.ModelForm):
    class Meta:
        model=BlogCategories
        exclude=['created_at']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Get the current choices for the parent field
        parent_choices = self.fields['parent'].choices
        # Get the current names of all BlogCategories objects in the database
        current_names = BlogCategories.objects.values_list('name', flat=True)
        # Create a new parent choice for each name that is not already a choice
        new_choices = [(name, name) for name in current_names if name not in dict(parent_choices)]
        # Add the new choices to the existing choices for the parent field
        self.fields['parent'].choices += new_choices

    def save(self, commit=True):
        # Save the instance to the database
        instance = super().save(commit=commit)
        # Get the current choices for the parent field
        parent_choices = self.fields['parent'].choices
        # Get the current names of all BlogCategories objects in the database
        current_names = BlogCategories.objects.values_list('name', flat=True)
        # Create a new parent choice for each name that is not already a choice
        new_choices = [(name, name) for name in current_names if name not in dict(parent_choices)]
        # Add the new choices to the existing choices for the parent field
        self.fields['parent'].choices += new_choices
        return instance




class TagsForm(forms.ModelForm):
    class Meta:
        model=Tags
        exclude=['created_at']

