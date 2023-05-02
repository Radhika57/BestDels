from django.shortcuts import render
from dashboard.models import *
from django.db.models import Q
from accounts.models import *
# Create your views here.



def maincontent(request):
    data = Properties.objects.all()
    if request.method == 'POST':
        country = request.POST.get('country')
        Type = request.POST.get('Type')
        status = request.POST.get('status')
        number_of_bedrooms = request.POST.get('number_of_bedrooms')
        number_of_bathrooms = request.POST.get('number_of_bathrooms')
       
        data = Properties.objects.filter(Q(country=country)|Q(Type=Type)
                                         |Q(status=status)|Q(number_of_bedrooms=number_of_bedrooms)
                                         |Q(number_of_bathrooms=number_of_bathrooms))
        return render(request,"accounts/index.html",{'data':data})
        
    return render(request,'accounts/index.html',{'Property':data})


def properties_list(request):
    property = Properties.objects.all()
    return render(request,'accounts/properties-list.html',{'property':property})
 
def project_list(request):
    project = Projects.objects.all()
    return render(request,'accounts/project-list.html',{'project':project})

def properties_by_city(request, city):
    properties = Properties.objects.filter(city=city)
    return render(request, 'accounts/properties-grid.html', {'properties': properties})

def propertySingleGallery(request,id):
    data = Properties.objects.get(id=id)
    if request.method == "POST":
        rating_value = request.POST.get('rating')
        try:
            rating_value = int(rating_value)
        except ValueError:
            rating_value = None
        name = request.POST.get('name')
        email = request.POST.get('email')
        reviews = request.POST.get('review')
        
        if rating_value is not None:
            review = PropertiesReviews(data=data, rating=rating_value,email=email, reviews=reviews,name=name)
            review.save()
    return render(request,'accounts/property-single-gallery.html',{"data":data})

def projectSingleGallery(request,id):
    data = Projects.objects.get(id=id)
    if request.method == "POST":
        rating_value = request.POST.get('rating')
        try:
            rating_value = int(rating_value)
        except ValueError:
            rating_value = None
        name = request.POST.get('name')
        email = request.POST.get('email')
        reviews = request.POST.get('review')
        
        if rating_value is not None:
            review = ProjectReviews(data=data, rating=rating_value,email=email, reviews=reviews,name=name)
            review.save()
        
    return render(request,'accounts/project-single.html',{"data":data})

def pageContact(request):
    if request.method == "POST":
        name = request.POST.get('contact-name')
        email = request.POST.get('contact-email')
        phonenumber = request.POST.get('phone-number')
        message = request.POST.get('contact-message')
        data = Contact_us(name=name,email=email,phonenumber=phonenumber,message=message)
        data.save()
    return render(request,'accounts/page-contact.html')

def pageAbout(request):
    return render(request,'accounts/page-about.html')

def pageFaq(request):
    faq = FAQ.objects.all()
    return render(request,'accounts/page-faq.html',{'faq':faq})

def privacypolicy(request):
    return render(request,'accounts/privacy-policy.html')

def termsconditions(request):
    return render(request,'accounts/terms-conditions.html')

# def projectreviews(request, project_id):
#     project = Projects.objects.get(id=project_id)
#     if request.method == "POST":
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         rating = request.POST.get('rating')
#         reviews = request.POST.get('review')
#         data = Reviews(project=project,name=name, email=email, rating=rating, reviews=reviews)
#         data.save()
#         return render(request, 'accounts/project-single.html', {'project': project})
#     return render(request, 'accounts/project-single.html', {'project': project})

def agencyprofile(request):
    return render(request,'accounts/agency-profile.html')

def agentprofile(request):
    return render(request,'accounts/agent-profile.html')

def agents(request):
    return render(request,'accounts/agents.html')

def blogsidebar(request):
    return render(request,'accounts/blog-sidebar-left.html')

def blogsingle(request):
    return render(request,'accounts/blog-single.html')

def blog(request):
    return render(request,'accounts/blog.html')

def favoriteproperty(request):
    return render(request,'accounts/favourite-properties.html')

def homeproperty(request):
    return render(request,'accounts/home-property.html')

def homesplash(request):
    return render(request,'accounts/home-splash.html')

def userProfile(request):
    return render(request,'accounts/user-profile.html')

def socialProfile(request):
    return render(request,'accounts/social-profile.html')

def propertySingleSlider(request):
    return render(request,'accounts/property-single-slider.html')


# def propertiesGrid(request):
#     return render(request,'accounts/properties-grid.html')

def propertiesGridSplit(request):
    return render(request,'accounts/properties-grid-split.html')

def page404(request):
    return render(request,'accounts/page-404.html')

def myProperties(request):
    return render(request,'accounts/my-properties.html')

