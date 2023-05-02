
from django.contrib import admin
from django.urls import path, include
from accounts import views
from dashboard import dashboard_views
from Useraccount.views import RegisterView,LoginView ,DealerRegisterView,DealerLoginView
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path("admin/", admin.site.urls),
    path("",views.maincontent,name='maincontent'),
    path("privacy/", views.privacypolicy,name='privacy'),
    path("termsconditions/", views.termsconditions,name='termsconditions'),
    path("agencyprofile/", views.agencyprofile,name='agencyprofile'),
    path("agentprofile/", views.agentprofile,name='agentprofile'),
    path("blogsidebar/", views.blogsidebar,name='blogsidebar'),
    path("blogsingle/", views.blogsingle,name='blogsingle'),
    path("blog/", views.blog,name='blog'),
    path("favoriteproperty/", views.favoriteproperty,name='favoriteproperty'),
    path("homeproperty/", views.homeproperty,name='homeproperty'),
    path("homesplash/", views.homesplash,name='homesplash'),
    path("userProfile/", views.userProfile,name='userProfile'),
    path("social/", views.socialProfile,name='socialProfile'),
    path("SingleSlider/", views.propertySingleSlider,name='propertySingleSlider'),
    path("SingleGrid/<int:id>", views.propertySingleGallery,name='propertySingleGallery'),
    path("SingleGridProject/<int:id>", views.projectSingleGallery,name='SingleGridProject'),
    # path("propertiesGrid/<int:city>", views.properties_by_city,name='propertiesGrid'),
    # path("propertiesGrid/", views.propertiesGrid,name='propertiesGrid'),
    path("GridSplit/", views.propertiesGridSplit,name='propertiesGridSplit'),
    path("FAQ/", views.pageFaq,name='pageFaq'),
    path("Contact/", views.pageContact,name='pageContact'),
    path("About/", views.pageAbout,name='pageAbout'),
    path("Error/", views.page404,name='page404'),
    path("MyProperties/", views.myProperties,name='myProperties'),
    path("propertieslist/", views.properties_list,name='propertieslist'),
    path("projectlist/", views.project_list,name='projectlist'),
    path("signup/",RegisterView.as_view(),name="signup"),
    path("login/",LoginView.as_view(),name="login"),
    path("DealerSignup/",DealerRegisterView.as_view(),name="dealerSignup"),
    path("DealerLogin/",DealerLoginView.as_view(),name="dealerLogin"),
    # path("projectreview/", views.projectreviews,name='projectreview'),
    
    
    #dashboard URLS
    path('',include('dashboard.urls')),
    # path('account/',include('Useraccount.urls')),
    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
