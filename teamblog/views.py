from teamblog.models import writePost
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import writePost

class HomeView(ListView):
    model = writePost
    template_name = 'home.html'

class ArticleDetailView(DetailView):
    model = writePost
    template_name = 'article_details.html'


