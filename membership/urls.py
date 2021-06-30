from django.urls import path
from .views import UserRegisterView, UserEditView, PasswordsChangeView
from django.contrib.auth import views as auth_views  #It allows using some of the views that come with the authentication system comes with django
from . import views

urlpatterns = [
    path('registeration/', UserRegisterView.as_view(), name='registeration'),
    path('edit_profile/', UserEditView.as_view(), name='edit-profile'),    
    #path('password/', auth_views.PasswordsChangeView.as_view(template_name='registration/change-password.html')),
    path('password/', PasswordsChangeView.as_view(template_name='registration/change-password.html')),
    path('password_success/', views.password_success, name='password_success.html'),
]
