from dataclasses import fields
from pyexpat import model
from django.shortcuts import render
from .models import *
from django.views.generic.edit import CreateView, DeleteView
# Create your views here.
def index(request):
    todos = Todo.objects.all()
    return render(request, 'index.html', {'todos':todos})

def detail(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    return render(request, 'detail.html',{'todo': todo})

class todoCreate(CreateView):
    model = Todo
    fields = '__all__'

class todoDelete(DeleteView):
    model = Todo
    success_url = '/'