from . import views
from django.urls import path, include

app_name = 'myprofile'

urlpatterns = [
path('', views.index, name = 'index'),
]