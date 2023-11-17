from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('course/', course),
    path('class/', cabinet),
]
