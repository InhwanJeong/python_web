from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('orm', views.orm_cook_book),
]