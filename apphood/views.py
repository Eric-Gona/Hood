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

class CreateNewPost(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'new_post.html'
    fields = ['title', 'content', 'picture']
    login_url = 'login'

    def form_valid(self, form):
        form.instance.profile = self.request.user
        form.instance.neighborhood = self.request.user
        return super().form_valid(form)


class CreateBusiness(LoginRequiredMixin, CreateView):
    model = Business
    template_name = 'new_business.html'
    fields = ['name', 'description','business_pic']
    login_url = 'login'

    def form_valid(self, form):
        form.instance.profile = self.request.user
        return super().form_valid(form)

class SinglePost(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'post-detail.html'
    login_url = 'login'


class UpdateProfile(UpdateView):
    model = Profile
    template_name = 'update_profile.html'


class BusinessPage(LoginRequiredMixin, ListView):
    model = Business
    template_name = 'business.html'
    login_url = 'login'