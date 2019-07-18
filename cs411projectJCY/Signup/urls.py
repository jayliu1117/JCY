from . import views
from django.urls import path, include

app_name = 'Signup'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('addperson/', views.addperson, name = 'addperson'),
    path('changepassword/', views.changepassword, name = 'changepassword'),
    path('updatepassword/', views.updatepassword, name = 'updatepassword'),
    path('deactivate_account/', views.deactivate_account, name= 'deactivate_account'),
    path('delete_account/', views.delete_account, name = 'delete_account'),
    path('forgetpassword/', views.forgetpassword, name = 'forgetpassword'),
    path('search_password', views.search_password, name = 'search_password')
    ]
