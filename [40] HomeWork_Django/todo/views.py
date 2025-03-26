from django.shortcuts import render
from . models import Task

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy

# login / logout
from django.contrib.auth.views import LoginView

# mixins
from django.contrib.auth.mixins import LoginRequiredMixin


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


  def form_valid(self, form):
    form.instance.user = self.request.user

    return super().form_valid(form)


class TaskUpdate(LoginRequiredMixin, UpdateView):
  model = Task
  fields = ['title' , 'description', 'complete']
  success_url = reverse_lazy('tasks')
  template_name = "todo/task_form_update.html"


class TaskDelete(LoginRequiredMixin, DeleteView):
  model = Task
  context_object_name = 'task'
  success_url = reverse_lazy('tasks')