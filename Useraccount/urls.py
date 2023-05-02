
from django.urls import path
from .views import *


path("signup/",RegisterView.as_view(),name="signup"),
path("login/",LoginView.as_view(),name="login"),
path("DealerSignup/",DealerRegisterView.as_view(),name="dealerSignup"),
path("DealerLogin/",DealerLoginView.as_view(),name="dealerLogin"),
# path('logout/<int:pk>/delete/', UserDeleteView.as_view(), name='my_logout'),

