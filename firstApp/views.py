from http.client import HTTPResponse
from django.views.generic.list import ListView
from django.shortcuts import render
from firstApp.models import Task
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
# from django.forms import ModelForm
from django.http import HttpResponseRedirect
# from django.contrib.auth.mixins import LoginRequiredMixin
# # Create your views here
from django.contrib.auth.mixins import LoginRequiredMixin

# class Authorized(LoginRequiredMixin):
#     def get_queryset(self):
#         return Task.objects.filter(user = self.request.user)

class ViewTask(LoginRequiredMixin, ListView):
    model= Task
    template_name= 'home.html'
    queryset= Task.objects.all()
    context_object_name= 'tasks'

    def get_queryset(self):
        return Task.objects.filter(user = self.request.user)

# class TaskForm(ModelForm):
#     class Meta:
#         model = Task
#         fields = ['title', 'completed', 'description']    

class CreateTask(CreateView):
    # form_class = TaskForm
    model= Task
    fields= ['title', 'completed', 'description']
    template_name= 'creation.html'
    success_url= '/home/'

    def form_valid(self, form):
        print("dekhle ")
        print(form)
        form.save()
        self.object= form.save()
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

class UpdateTask(UpdateView):
    model= Task
    fields= ['title', 'description']
    template_name= 'update.html'
    success_url= '/home/'

class DeleteTask(DeleteView):
    model= Task
    template_name= 'delete.html'
    success_url= '/home/'

class SignUp(CreateView):
    form_class= UserCreationForm
    success_url= '/login/'
    template_name= 'signup.html'

class Login(LoginView):
    success_url= '/login/'
    template_name= 'signup.html'
    