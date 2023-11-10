from django.urls import path
from . import views

# place the url paths here 

urlpatterns = [
    # Add task feature
    path('addTask/', views.addTask, name='addTask'), 

    # Mark as done feature
    path('mark_as_done/<int:pk>/', views.mark_as_done, name='mark_as_done'),

    # mark as undone feature
    path('mark_as_undone/<int:pk>/', views.mark_as_undone, name='mark_as_undone'),

    # Edit feature
    path('edit_task/<int:pk>', views.edit_task, name='edit_task'),
]
