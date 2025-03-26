from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from . models import Task 
from django.contrib.auth.views import LoginView               # login / logout
from django.contrib.auth.mixins import LoginRequiredMixin     # mixins
from django.contrib.auth.forms import UserCreationForm        # for Registration
from django.contrib.auth import login


class RegisterPage(FormView):
    template_name = 'todo/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()

        if user is not None:
            login(self.request, user)

        return super().form_valid(form)
    
    def get(self, *args, **kwargs):

        if self.request.user.is_authenticated:
            return redirect('tasks')

        return super().get(*args, **kwargs)



class CustomLoginView(LoginView):
  template_name = 'todo/login.html'

  def get_success_url(self):
    return reverse_lazy('tasks')
  
  
class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(complete=False).count()
        # print(context['tasks'])

        search_input = self.request.GET.get('search_area') or ''

        if search_input:
            #  context['tasks'] = context['tasks'].filter(title__icontines=search_input)
             context['tasks'] = context['tasks'].filter(title__startswith=search_input)
             context['search_input'] = search_input


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
