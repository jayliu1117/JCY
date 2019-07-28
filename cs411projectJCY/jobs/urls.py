from . import views
from django.urls import path, include

app_name = 'jobs'
urlpatterns = [
path('', views.index, name = 'index'),
]