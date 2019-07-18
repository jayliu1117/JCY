from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.index, name = 'index'),
    path('count/', views.count_registrations, name = 'count_registrations'),
    path('addperson/', include("Signup.urls")),
    path('competitors/', views.count_competitors, name = 'count_competitors')
]