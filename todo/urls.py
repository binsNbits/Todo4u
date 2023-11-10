from django.urls import path
from . import views

# place the url paths here 

urlpatterns = [
    path('addTask/', views.addTask, name='addTask'), 
     path('mark_as_done/<int:pk>/', views.mark_as_done, name='mark_as_done'),
]
