from . import views
from django.urls import path, include

app_name = 'myprofile'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('coursetable/', views.coursetale, name = 'coursetable'),
    path('count_reg/', views.count_reg, name = 'count_reg'),
]