from django.urls import path
from .views import *


urlpatterns = [
   path('enquieryadd/',enquieryCreate.as_view())
]