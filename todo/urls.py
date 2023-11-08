from django.urls import path
from . import views

# place the url paths here 

urlpatterns = [
    path('addTask/', views.addTask, name='addTask')
]
