from django.urls.base import reverse_lazy
from teamblog.models import Post, Category
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Category, Post
from .forms import PostForm, EditForm
from django.urls import reverse_lazy

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-created_date'] # OR ordering = ['-id'] -id: the latest one comes the first on the home page

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

def CategoryListView(request):
    cat_menu_list = Category.objects.all() #quering the database here and grabbing all of our category names
    return render(request, 'category_list.html', {'cat_menu_list':cat_menu_list})


def CategoryView(request, cats):  #request is a url
    category_posts = Post.objects.filter(category__iexact=cats.replace('-',' '))
    return render(request, 'categories.html', {'cats':cats.title().replace('-', ' '), 'category_posts':category_posts})   #'cats':cats.title() => strange. not to change capital letter


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    #fields = '__all__'
    #fields = ('title', 'body')
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(AddPostView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context    

class AddCategoryView(CreateView):
    model = Category
    template_name = 'add_category.html'
    fields = '__all__'
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(AddCategoryView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context    

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(UpdatePostView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context        

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(DeletePostView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context        
