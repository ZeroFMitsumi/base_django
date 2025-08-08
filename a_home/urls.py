from django.urls import path
from .views import *

app_name = 'a_home'

urlpatterns = [
    path('', home_view, name='home'),
]