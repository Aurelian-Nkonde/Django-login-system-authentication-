from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .forms import RegisterForm

class Register(CreateView):
    template_name = 'signup.html'
    form_class = RegisterForm
    success_url = reverse_lazy('login')
    context_object_name = 'register'





