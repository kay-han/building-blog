
from django.urls import path
from .views import HomeView 
from .views import ArticleDetailView
from .views import AddPostView
from .views import UpdatePostView
from .views import DeletePostView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
    path('add_post/', AddPostView.as_view(), name='add-post'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name='update-post'),
    path('article/<int:pk>/remove', DeletePostView.as_view(), name='delete-post'),
]
