from django.urls import path
from .views import *

urlpatterns = [
    path('about-setting/',AboutModelView.as_view(),name = 'about-setting'),
    path('contact-us/',ContactUsModelView.as_view(),name='contact-us'),
    path('contact-images/',ContactSettingModelView.as_view(),name='contact-images')   
]