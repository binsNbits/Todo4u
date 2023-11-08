from django.shortcuts import render
from todo.models import Task


def home(request):
    task = Task.objects.filter(is_completed = False)
    print(task)
    context = {
        'tasks' : task,
    }
    return render(request, 'home.html', context)