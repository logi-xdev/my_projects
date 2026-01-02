from django.shortcuts import render

def home(request):
    return render(request, 'main/home.html')

def task_list(request):
    return render(request, 'main/tasks.html')

def add_task(request):
    return render(request, 'main/add_task.html')
