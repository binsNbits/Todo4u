from django.urls import path
from . import views

# place the url paths here 

urlpatterns = [
    # Add task feature
    path('addTask/', views.addTask, name='addTask'), 

    # Mark as done feature
    path('mark_as_done/<int:pk>/', views.mark_as_done, name='mark_as_done'),

    # Edit feature
    path('edit_task/<int:pk>/', views.edit_task, name='edit_task'),

    #Delete task feature
    path('delete_task/<int:pk>/', views.delete_task, name='delete_task'),
]
