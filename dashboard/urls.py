from django.contrib import admin
from django.urls import path,include
from dashboard import dashboard_views



urlpatterns = [
    
    path("dashboard/",dashboard_views.dashboard,name='dashboard'),
    path("AddProperty/",dashboard_views.AddProperty,name='addProperty'),
    path("CreateFacility/",dashboard_views.CreateFacility,name='createFacility'),
    path("AddInvestors/",dashboard_views.AddInvestors,name='addInvestors'),
    path("AddProject/",dashboard_views.AddProjects,name='addProject'),
    path("projects/",dashboard_views.projects,name='projects'),
    path("property/",dashboard_views.property,name='property'),
    path("facility/",dashboard_views.facility,name='facility'),
    path("investor/",dashboard_views.investors,name='investor'),
    path("features/",dashboard_views.features,name='features'),
    path("categories/",dashboard_views.categories,name='categories'),
    path("AddCategories/",dashboard_views.AddCategories,name='addCategories'),
    path("AddFeatures/",dashboard_views.AddFeatures,name='addFeatures'),
    path("Testimonial/",dashboard_views.Testimonial,name='Testimonial'),
    path("AddTestimonial/",dashboard_views.AddTestimonials,name='addTestimonial'),
    path("AddCity/",dashboard_views.AddCity,name='addCity'),
    path("City/",dashboard_views.City,name='City'),
    path('deletecity/<int:id>',dashboard_views.deletecity,name="deletecity"),
    
    
    # path("AddReviews/",dashboard_views.AddReviews,name='addReviews'),
    # path("reviews/",dashboard_views.Review,name='reviews'),
    path("AddFAQ/",dashboard_views.AddFAQ,name='addFAQ'),
    path("faq/",dashboard_views.faq,name='FAQ'),
    path("AddPosts/", dashboard_views.AddPosts,name='addPosts'),
    path("posts/", dashboard_views.Post,name='Posts'),
    path("AddBlogCategories/", dashboard_views.AddBlogCategories,name='addBlogCategories'),
    path("AddTags/", dashboard_views.AddTags,name='addTags'),
    path("Tags/", dashboard_views.Tag,name='Tags'),
    path("editproperty/<int:pk>", dashboard_views.PropertyUpdateView.as_view(), name="editproperty"),
    path("editProject/<int:pk>", dashboard_views.ProjectUpdateView.as_view(), name="editProject"),
    path("editfacility/<int:pk>", dashboard_views.FacilityUpdateView.as_view(), name="editfacility"),
    path("editinvestor/<int:pk>", dashboard_views.InvestorsUpdateView.as_view(), name="editinvestor"),
    path("editcategories/<int:pk>", dashboard_views.CategoriesUpdateView.as_view(), name="editcategories"),
    path("editfeatures/<int:pk>", dashboard_views.FeaturesUpdateView.as_view(), name="editfeatures"),
    # path("editreview/<int:pk>", dashboard_views.ReviewsUpdateView.as_view(), name="editreview"),
    path("editpost/<int:pk>", dashboard_views.PostsUpdateView.as_view(), name="editpost"),
    path("edittag/<int:pk>", dashboard_views.TagsUpdateView.as_view(), name="edittag"),
    path("editfaq/<int:pk>", dashboard_views.FAQUpdateView.as_view(), name="editfaq"),
    path("edittestimonial/<int:pk>", dashboard_views.TestimonialsUpdateView.as_view(), name="edittestimonial"),
    path('deleteproperty/<int:id>',dashboard_views.deleteProperty,name="deleteproperty"),
    path('deleteproject/<int:id>',dashboard_views.deleteProject,name="deleteproject"),
    path('deletefacility/<int:id>',dashboard_views.deletefacility,name="deletefacility"),
    path('deleteinvestor/<int:id>',dashboard_views.deleteinvestor,name="deleteinvestor"),
    path('deletecategory/<int:id>',dashboard_views.deletecategory,name="deletecategory"),
    path('deletefeature/<int:id>',dashboard_views.deletefeature,name="deletefeature"),
    path('deletetestimonial/<int:id>',dashboard_views.deletetestimonial,name="deletetestimonial"),
    # path('deletereview/<int:id>',dashboard_views.deletereview,name="deletereview"),
    path('deletepost/<int:id>',dashboard_views.deletepost,name="deletepost"),
    path('deletetag/<int:id>',dashboard_views.deletetag,name="deletetag"),
    path('deletefaq/<int:id>',dashboard_views.deletefaq,name="deletefaq"),


#DEALER PROPERTY
    path("ADDPROPERTY/",dashboard_views.AddDealerProperty,name='ADDPROPERTY'),
    path("PROPERTY/",dashboard_views.DealerProperty,name='PROPERTY'),
    path("success/",dashboard_views.Success,name='success'),
    

]
