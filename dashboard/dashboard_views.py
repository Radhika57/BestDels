from django.shortcuts import render,redirect
from .forms import *
from django.views.generic import TemplateView,UpdateView
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from django.http import HttpResponseRedirect
import razorpay
from property_dealing_app.settings import razor_pay_key_id,key_secret
from django.views.decorators.csrf import csrf_exempt 

# Create your views here.
def dashboard(request):
    return render(request,'dashboard/demo.html')

def AddCity(request):
    form = CityForm()
    if request.method == 'POST':
        form = CityForm(request.POST)
       
        if form.is_valid():
            
            form.save()
        else:
            return render (request,'dashboard/addcity.html', {'error': form.errors})
    return render(request, 'dashboard/addcity.html',{'form':form})

def City(request):
    City = city.objects.all()
    return render(request,"dashboard/city.html",{'City':City})

def deletecity(request,id):
    City = city.objects.get(id=id)
    City.delete()
    return HttpResponseRedirect(reverse('City'))

def AddProperty(request):
    form = PropertiesForm()
    formset = BirdFormSet(queryset=Facilities.objects.none())
   
    if request.method == 'POST':
            formset = BirdFormSet(request.POST)
        
            if formset.is_valid():
                list=[]
                for i in formset:
                    inst = i.save()
                    list.append(inst.id)
            form = PropertiesForm(request.POST,request.FILES)
            if form.is_valid():
                
                instance = form.save(commit=False)
                instance.user=request.user
                instance.save()
                m = Properties.objects.filter().last()
                m.facility.set(list)
            else:
                return render (request,'dashboard/addProperty.html', {'error': form.errors})
    return render(request, 'dashboard/addProperty.html',{'form':form,"bird_formset":formset})

def AddDealerProperty(request):
    form = DealerPropertiesForm()
    formset = BirdFormSet(queryset=Facilities.objects.none())
   
    if request.method == 'POST':
            formset = BirdFormSet(request.POST)
        
            if formset.is_valid():
                list=[]
                for i in formset:
                    inst = i.save()
                    list.append(inst.id)
            form = DealerPropertiesForm(request.POST,request.FILES)
            if form.is_valid():
                
                instance = form.save(commit=False)
                instance.user=request.user
                instance.save()
                m = Properties.objects.filter().last()
                m.facility.set(list)
            else:
                return render (request,'PropertyDealer/ADDPROPERTY.html', {'error': form.errors})
    return render(request, 'PropertyDealer/ADDPROPERTY.html',{'form':form,"bird_formset":formset})

class BirdAddView(TemplateView):
    template_name = "addProperty.html"

    def get(self, *args, **kwargs):
        formset = BirdFormSet(queryset=Facilities.objects.none())
        form = PropertiesForm()
        return self.render_to_response({"bird_formset": formset,'form':form})

    def post(self, *args, **kwargs):

        formset = BirdFormSet(data=self.request.POST)

        if formset.is_valid():
           instance2=formset.save()
        form = PropertiesForm(data=self.request.POST)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.created_by=self.request.user
            instance.save()
            m = Properties.objects.filter().last()
            m.facility.add(instance2.id)
            return redirect(reverse_lazy("bird_list"))

        return self.render_to_response({"bird_formset": formset})

def property(request):
    property = Properties.objects.all()
    return render(request,"dashboard/properties.html",{'property':property})


def DealerProperty(request):
    type = request.user.type
    if type == "Admin":
        PROPERTY= Properties.objects.all()  
    else:
        PROPERTY = Properties.objects.filter(user__email=request.user.email)
        client=razorpay.Client(auth =("rzp_test_c9U71b8iZvSlxi" , "DkSl2ey8clwF0dtmPlq73QUe"))
            
        payment=client.order.create({'amount':10000, 'currency':'INR' , 'payment_capture':'1'})
        return render(request,"PropertyDealer/PROPERTY.html",{'PROPERTY':PROPERTY,'payment':payment})

@csrf_exempt
def Success(request):
 if request.method=="POST":
    a=request.POST
    # print(a)
    order_id=""
    for key,val in a.items():
        if key=="razorpay_order_id":
            order_id = val
        break
    print(a["razorpay_payment_id"])
    # user=Payment.objects.create(payment_id=a["razorpay_order_id"])
    # #  user.paid=True
    # user.save()
 return render(request , 'PropertyDealer/success.html')

def AddProjects(request):
    form = ProjectsForm()
    formset = BirdFormSet(queryset=Facilities.objects.none())
    if request.method == 'POST':
        formset = BirdFormSet(request.POST)
        
        if formset.is_valid():
                list=[]
                for i in formset:
                    inst = i.save()
                    list.append(inst.id)
        form = ProjectsForm(request.POST,request.FILES)
       
        if form.is_valid():
           
            instance = form.save(commit=False)
            instance.user=request.user
            instance.save()
            m = Projects.objects.filter().last()
            m.facility.set(list)
        else:
            return render (request,'dashboard/addProjects.html', {'error': form.errors})
    return render(request, 'dashboard/addProjects.html',{'form':form,"bird_formset":formset})

def projects(request):
    project = Projects.objects.all()
    return render(request,"dashboard/projects.html",{'project':project})


def CreateFacility(request):
    form = FacilitiesForm()
    if request.method == 'POST':
        form = FacilitiesForm(request.POST)
       
        if form.is_valid():
            
            form.save()
        else:
            return render (request,'dashboard/createFacility.html', {'error': form.errors})
    return render(request, 'dashboard/createFacility.html',{'form':form})

def facility(request):
    facility = Facility.objects.all()
    return render(request,"dashboard/facility.html",{'facility':facility})

def AddInvestors(request):
    form = InvestorsForm()
    if request.method == 'POST':
        form = InvestorsForm(request.POST)
       
        if form.is_valid():
            
            form.save()
        else:
            return render (request,'dashboard/addinvestors.html', {'error': form.errors})
    return render(request, 'dashboard/addinvestors.html',{'form':form})

def investors(request):
    investors = Investors.objects.all()
    return render(request,"dashboard/investors.html",{'investors':investors})

def features(request):
    features = Features.objects.all()
    return render(request,"dashboard/featureslist.html",{'features':features})

def categories(request):
    categories = Categories.objects.all()
    return render(request,"dashboard/categorieslist.html",{'categories':categories})

def AddCategories(request):
    form = CategoriesForm()
    if request.method == 'POST':
        form = CategoriesForm(request.POST)
       
        if form.is_valid():
            
            form.save()
        else:
            return render (request,'dashboard/categories.html', {'error': form.errors})
    return render(request, 'dashboard/categories.html',{'form':form})


def AddFeatures(request):
    form = FeaturesForm()
    if request.method == 'POST':
        form = FeaturesForm(request.POST)
       
        if form.is_valid():
            
            form.save()
        else:
            return render (request,'dashboard/features.html', {'error': form.errors})
    return render(request, 'dashboard/features.html',{'form':form})

def AddFAQ(request):
    form = FAQForm()
    if request.method == 'POST':
        form = FAQForm(request.POST)
       
        if form.is_valid():
            
            form.save()
        else:
            return render (request,'dashboard/addFAQ.html', {'error': form.errors})
    return render(request, 'dashboard/addFAQ.html',{'form':form})


def faq(request):
    faq = FAQ.objects.all()
    return render(request,"dashboard/faq.html",{'faq':faq})

# def AddReviews(request):
    
#     form = ReviewForm()
#     if request.method == 'POST':
#         form = ReviewForm(request.POST)
       
#         if form.is_valid():
            
#             form.save()
#         else:
#             return render (request,'dashboard/addreviews.html', {'error': form.errors})
#     return render(request, 'dashboard/addreviews.html',{'form':form})

# def AddReviews(request):
#     form = ReviewForm()
#     if request.method == 'POST':
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             # get the selected project
#             project_id = form.cleaned_data['project_name']
#             project = Projects.objects.get(id=project_id)
#             # create the review with the project foreign key
#             review = form.save(commit=False)
#             review.project_name = project
#             review.save()
#             return redirect('review_list')
#         else:
#             return render(request, 'dashboard/addreviews.html', {'error': form.errors})
#     return render(request, 'dashboard/addreviews.html', {'form': form})

# def Review(request):
#     reviews = Reviews.objects.all()
#     return render(request,"dashboard/reviews.html",{'reviews':reviews})


def AddTestimonials(request):
    form = TestimonialsForm()
    if request.method == 'POST':
        form = TestimonialsForm(request.POST,request.FILES)
       
        if form.is_valid():
            
            form.save()
        else:
            return render (request,'dashboard/addTestimonial.html', {'error': form.errors})
    return render(request, 'dashboard/addTestimonial.html',{'form':form})

def Testimonial(request):
    testimonial = Testimonials.objects.all()
    return render(request,"dashboard/testimonial.html",{'testimonial':testimonial})


def AddPosts(request):
    form = PostsForm()
    if request.method == 'POST':
        form = PostsForm(request.POST,request.FILES)
       
        if form.is_valid():
            
            form.save()
        else:
            return render (request,'dashboard/addPosts.html', {'error': form.errors})
    return render(request, 'dashboard/addPosts.html',{'form':form})

def Post(request):
    posts=Posts.objects.all()
    return render(request,'dashboard/post.html',{'posts':posts})


def AddBlogCategories(request):
    form = BlogCategoriesForm()
    if request.method == 'POST':
        form = BlogCategoriesForm(request.POST)
       
        if form.is_valid():
            
            form.save()
        else:
            return render (request,'dashboard/addBlogCategories.html', {'error': form.errors})
    return render(request, 'dashboard/addBlogCategories.html',{'form':form})

def AddTags(request):
    form = TagsForm()
    if request.method == 'POST':
        form = TagsForm(request.POST)
       
        if form.is_valid():
            
            form.save()
        else:
            return render (request,'dashboard/addTags.html', {'error': form.errors})
    return render(request, 'dashboard/addTags.html',{'form':form})


def Tag(request):
    tags=Tags.objects.all()
    return render(request,'dashboard/tags.html',{'tags':tags})

class PropertyUpdateView(UpdateView):
    template_name = 'dashboard/editProperty.html'
    model = Properties
    fields = ['Title','Type','description','content','image','country','state','city','property_location',
              'Latitude','Longitude','number_of_bedrooms','number_of_bathrooms','number_of_floors',
              'square','price','currency','status','moderation_status','unique_id','apartment',
              'villa','condo','house','land','commercial_property','project','account','wifi','parking',
              'swimming_pool','balcony','garden','security','fitness_center','air_conditioning','central_heating',
              'laundary_room','pets','spa_massage']
    success_url ="/property/"
    
    
class ProjectUpdateView(UpdateView):
    template_name = 'dashboard/editProject.html'
    model = Projects
    fields = ['Name','description','content','image','country','state','city','project_location',
              'Latitude','Longitude','number_of_blocks','number_of_floors','number_of_flats',
              'low_price','max_price','currency','status','unique_id','apartment',
              'villa','condo','house','land','commercial_property','investors','finish_date',
              'sell_date','wifi','parking','swimming_pool','balcony','garden','security',
              'fitness_center','air_conditioning','central_heating','laundary_room','pets','spa_massage']
    success_url ="/projects/"
    
    
class FacilityUpdateView(UpdateView):
    template_name = 'dashboard/editfacility.html'
    model = Facility
    fields = ['name','icon','status']
    success_url ="/facility/"
    
class InvestorsUpdateView(UpdateView):
    template_name = 'dashboard/editinvestor.html'
    model = Investors
    fields = ['name','status']
    success_url ="/investor/"
    
class CategoriesUpdateView(UpdateView):
    template_name = 'dashboard/editcategories.html'
    model = Categories
    fields = ['name','parent','description','order','status']
    success_url ="/categories/"
    
class FeaturesUpdateView(UpdateView):
    template_name = 'dashboard/editfeatures.html'
    model = Features
    fields = ['name','icon']
    success_url ="/features/"
    
# class ReviewsUpdateView(UpdateView):
#     template_name = 'dashboard/editreview.html'
#     model = Reviews
#     fields = ['author','reviewalble','content','rating','status']
#     success_url ="/reviews/"
    
class TestimonialsUpdateView(UpdateView):
    template_name = 'dashboard/edittestimonial.html'
    model = Testimonials
    fields = ['name','position','content','status','image']
    success_url ="/Testimonial/"
    
class PostsUpdateView(UpdateView):
    template_name = 'dashboard/editpost.html'
    model = Posts
    fields = ['name','description','content','status','image','categories']
    success_url ="/posts/"

class TagsUpdateView(UpdateView):
    template_name = 'dashboard/edittag.html'
    model = Tags
    fields = ['name','description','status']
    success_url ="/Tags/"
    
class FAQUpdateView(UpdateView):
    template_name = 'dashboard/editfaq.html'
    model = FAQ
    fields = ['category','questions','answer','status']
    success_url ="/faq/"
    
from django.urls import reverse
def deleteProperty(request,id):
    lead = Properties.objects.get(id=id)
    lead.delete()
    return HttpResponseRedirect(reverse('property'))

def deleteProject(request,id):
    lead = Projects.objects.get(id=id)
    lead.delete()
    return HttpResponseRedirect(reverse('projects'))

def deletefacility(request,id):
    lead = Facility.objects.get(id=id)
    lead.delete()
    return HttpResponseRedirect(reverse('facility'))

def deleteinvestor(request,id):
    lead = Investors.objects.get(id=id)
    lead.delete()
    return HttpResponseRedirect(reverse('investor'))

def deletecategory(request,id):
    lead = Categories.objects.get(id=id)
    lead.delete()
    return HttpResponseRedirect(reverse('categories'))

def deletefeature(request,id):
    lead = Features.objects.get(id=id)
    lead.delete()
    return HttpResponseRedirect(reverse('features'))

def deletetestimonial(request,id):
    lead = Testimonials.objects.get(id=id)
    lead.delete()
    return HttpResponseRedirect(reverse('Testimonial'))

# def deletereview(request,id):
#     lead = Reviews.objects.get(id=id)
#     lead.delete()
#     return HttpResponseRedirect(reverse('reviews'))

def deletepost(request,id):
    lead = Posts.objects.get(id=id)
    lead.delete()
    return HttpResponseRedirect(reverse('Posts'))

def deletetag(request,id):
    lead = Tags.objects.get(id=id)
    lead.delete()
    return HttpResponseRedirect(reverse('Tags'))

def deletefaq(request,id):
    lead = FAQ.objects.get(id=id)
    lead.delete()
    return HttpResponseRedirect(reverse('FAQ'))


