from whoisapp.views import MainApp
from django.urls import path
from .views import *

urlpatterns = [
    path('', MainApp, name="mainapp")

]