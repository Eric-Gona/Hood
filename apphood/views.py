from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView
from .models import Profile, Post, Business, Neighborhood
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class HomePage(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-pub_date']
    login_url = 'login'


class ProfilePage(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'
    login_url = 'login'
