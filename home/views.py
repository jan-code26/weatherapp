import imp
from re import template
from django.shortcuts import render
from datetime import datetime
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView
from django.shortcuts import redirect
class createuser(CreateView):
    form_class=UserCreationForm
    template_name='home/register.html'
    success_url='/notes'

    def get(self,request,*args,**kwargs):
        if(self.request.user.is_authenticated):
            return redirect("notes.list")
        return super().get(request,*args,**kwargs)
class loginuser(LoginView):
    template_name='home/login.html'
class logoutuser(LogoutView):
    template_name='home/logout.html'
class HomeView(TemplateView):
    template_name='home/welcome.html'
    extra_content={'today':datetime.today()}

class AuthorizedView(LoginRequiredMixin,TemplateView):
    template_name='home/authorized.html'
    login_url='/admin'
