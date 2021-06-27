
from django.urls import path
from .views import HomeView
from .views import ArticleDetailView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
]
