from . import views
from django.urls import path, include

app_name = 'Signup'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('addperson/', views.addperson, name = 'addperson'),
    ]
