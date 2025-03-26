from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from . models import Task 
from django.contrib.auth.views import LoginView # login / logout
from django.contrib.auth.mixins import LoginRequiredMixin # mixins


class CustomLoginView(LoginView):
  template_name = 'todo/login.html'

  def get_success_url(self):
    return reverse_lazy('tasks')
  
  
class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user, complete=False)

        print(context['tasks'])

        return context
    

class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    template_name = "todo/task.html"
    context_object_name = 'task'


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title' , 'description', 'complete']
    # fields = '__all__'
    success_url = reverse_lazy('tasks')


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title' , 'description', 'complete']
    # fields = '__all__'  # რაც მინდა შეიცვალოს
    template_name = 'todo/task_form.html'  # გამოვიყენე იგივე თარგი, რაც Create-ისთვის
    success_url = reverse_lazy('tasks')

class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = reverse_lazy('tasks')
    template_name = 'todo/task_confirm_delete.html'  # ახალი თარგი დასტურისთვის

# Create your views here.
