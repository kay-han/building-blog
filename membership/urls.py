from django.urls import path
from .views import UserRegisterView

urlpatterns = [
    path('registeration/', UserRegisterView.as_view(), name='registeration'),
]
