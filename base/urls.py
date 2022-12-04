from django.urls import path
from .views import create_user, home

urlpatterns = [
  path('', home, name="home"),
  path('apply/', create_user, name="create_user")
]