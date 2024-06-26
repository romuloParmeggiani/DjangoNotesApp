# from django.shortcuts import render
# from django.contrib.auth.decorators import login_required
from datetime import datetime

from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView


# Replaced below function-based views by following class-based views
# def home(request):
#     return render(request, 'home/welcome.html', {'today': datetime.today()})


# @login_required(login_url='/admin')
# def authorized(request):
#     return render(request, 'home/authorized.html', {})


class HomeView(TemplateView):
    template_name = 'home/welcome.html'
    extra_context = {'today': datetime.today()}


class LoginInterfaceView(LoginView):
    template_name = 'home/login.html'


class LogoutInterfaceView(LogoutView):
    template_name = 'home/logout.html'


class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = 'home/signup.html'
    success_url = 'smart/notes'
