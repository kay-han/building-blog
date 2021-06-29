from django.urls import path
from .views import UserRegisterView, UserEditView

urlpatterns = [
    path('registeration/', UserRegisterView.as_view(), name='registeration'),
    path('edit_profile/', UserEditView.as_view(), name='edit-profile'),    
]
