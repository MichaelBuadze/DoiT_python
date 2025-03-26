from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from . models import Task 


class TaskList(ListView):
    model = Task
    context_object_name = 'tasks'

class TaskDetail(DetailView):
    model = Task
    template_name = "todo/task.html"
    context_object_name = 'task'


class TaskCreate(CreateView):
    model = Task
    # fields = ['title', 'description']
    fields = '__all__'
    success_url = reverse_lazy('tasks')


class TaskUpdate(UpdateView):
    model = Task
    fields = '__all__'  # რაც მინდა შეიცვალოს
    template_name = 'todo/task_form.html'  # გამოვიყენე იგივე თარგი, რაც Create-ისთვის
    success_url = reverse_lazy('tasks')

class TaskDelete(DeleteView):
    model = Task
    success_url = reverse_lazy('tasks')
    template_name = 'todo/task_confirm_delete.html'  # ახალი თარგი დასტურისთვის

# Create your views here.
