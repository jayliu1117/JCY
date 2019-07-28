from . import views
from django.urls import path, include

app_name = 'ResearchArea'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('count_regis', views.count_regis, name = 'count_regis'),

]