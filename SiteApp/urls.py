from django.urls import path
from .views import *

urlpatterns = [
    path('',home_site,name='site')
]