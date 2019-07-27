from . import views
from django.urls import path, include

app_name = 'homepage'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('count/', views.count_registrations, name = 'count_registrations'),
    #path('addperson/', include("Signup.urls")),
    path('competitors/', views.count_competitors, name='count_competitors'),
    path('home_aftersignin/', views.home_aftersignin, name='home_after_signin'),
    path('count_regi/', views.count_regi, name = 'count_regi'),
    #path('gotoprofile/', views.gotoprofile, name='gotoprofile'),
    #path('profile/', views.profile, name='profile',)
    #path('fetchcoursedata', views.fetchcoursedata, name='fetchcoursedata'),
]