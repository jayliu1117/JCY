from . import views
from django.urls import path, include

app_name = 'Signin'
urlpatterns = [
    path('', views.index, name = 'index'),
    # path('changepassword/', views.changepassword, name = 'changepassword'),
    # path('updatepassword/', views.updatepassword, name = 'updatepassword'),

]
