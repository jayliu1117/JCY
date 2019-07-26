from . import views
from django.urls import path, include

app_name = 'Signin'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('login/', views.login, name='login'),
    path('gotoprofile/', views.gotoprofile, name = 'gotoprofile'),
    path('logoff/', views.logoff, name = 'logoff'),
    path('addCourse/<int:course_id>', views.addCourse, name='addCourse'),
    path('deleteCourse/<int:course_id>', views.deleteCourse, name = 'deleteCourse'),
    #path('profile/', views.profile, name='profile'),
    # path('changepassword/', views.changepassword, name = 'changepassword'),
    # path('updatepassword/', views.updatepassword, name = 'updatepassword'),

]
