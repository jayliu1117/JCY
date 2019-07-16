from django.shortcuts import render
from . import  models
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'Signup/signup.html')

def addperson(request):
    if request.method == 'POST':
        temp_email = request.POST.get('UIUC Email Address')
        temp_password = request.POST.get('Password')
        temp_major = request.POST.get('major')
        temp_skills = request.POST.get('skills')
        temp_interests = request.POST.get('interests')
        temp_student = models.Students(EmailAddress = temp_email, PassWord = temp_password, major = temp_major, skills = temp_skills, interests = temp_interests)
        temp_student.save()
        return HttpResponse("<h2>You are successfully registered!</h2>")