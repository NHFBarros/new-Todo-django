import os

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from .models import *

from djangoteste.settings import BASE_DIR

# Create your views here.
def todo(request):
    todos = Todo.objects.all()
    return render(request, 'todoDashboard.html', {'todos' : todos})


def todoAdd(request):
    if request.method == "GET":
        return render(request, 'todoAdd.html')
    elif request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        due_date = request.POST.get('due_date')
        priority = request.POST.get('priority')
        done = False

        todo = Todo.objects.filter(title=title)

        if todo.exists():
            return HttpResponse('Esse aí ta já feito pai')
        

        todo = Todo(
            title = title,
            description = description,
            due_date = due_date,
            priority = priority,
            done = done
        )

        todo.save()
        return redirect('todo')

    return redirect('todo')

def todoDone(request, id):
    if request.method == "POST":
        todo = get_object_or_404(Todo, id=id)
        todo.done = not todo.done
        todo.save()
        return redirect('todo')

    return redirect('todo')

def todoDelete(request, id):
    if request.method == "DELETE":
        todo = get_object_or_404(Todo, id=id)
        todo.delete()
        return redirect('todo')

    return redirect('todo')

def todoEdit(request, id):
    