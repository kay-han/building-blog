from django.urls.base import reverse_lazy
from teamblog.models import Post
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm, EditForm
from django.urls import reverse_lazy

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-created_date'] # OR ordering = ['-id'] -id: the latest one comes the first on the home page

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    
    #fields = '__all__'
    #fields = ('title', 'body')
    
class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'
    #fields = ['title', 'title_tag', 'body']

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

