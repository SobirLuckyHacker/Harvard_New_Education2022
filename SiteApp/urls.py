from django.urls import path
from .views import *

urlpatterns = [
    path('',home_site,name='site'),
    path('all_user/',all_users)
]