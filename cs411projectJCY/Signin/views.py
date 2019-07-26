from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.db import connection
# from ..Signup.models import Students
from django.http import HttpResponseRedirect
from homepage.models import Courses
from django.urls import  reverse
from myprofile.models import  hasTaken

temp_var =  [" "]
# Create your views here.
def index(request):
    return render(request, 'Signin/signin.html')
# def changepassword(request):
#     return render(request, 'Signin/changepassword.html')

# def updatepassword(request):
#     if request.method == 'POST':
#         temp_email = request.POST.get('UIUC Email Address')
#         temp_oldpassword = request.POST.get('Enter your old Password')
#         temp_newpassword = request.POST.get('Enter your new Password')
#         temp_confirm = request.POST.get('Enter your new Password again')
#         # with connection.cursor() as cursor:
#             # cursor.execute("select PassWord from signup_students where EmailAddress = %s", (temp_email,))
#             # row = cursor.fetchone()
#
#         if row == temp_oldpassword and temp_newpassword == temp_confirm:
#             with connection.cursor() as cursor:
#                 cursor.execute("update signup_students set PassWord = %s where EmailAddress = %s;", (temp_newpassword, temp_email))
#     return HttpResponse("<h2>Your PassWord is successfully changed </h2>")
def login(request):
    if request.method == 'POST':
        temp_email = request.POST.get('UIUC Email Address')
        temp_password = request.POST.get('Password')
        with connection.cursor() as cursor:
            cursor.execute("select PassWord from signup_students where EmailAddress  = %s;", (temp_email,))
            data = cursor.fetchone()
            print(data)
        if data[0] == temp_password:
            with connection.cursor() as cursor:
                cursor.execute("select EmailAddress from signup_students where EmailAddress = %s", (temp_email,))
                row = cursor.fetchone()
                temp_var[0] = row[0]
                print(row[0])
            #return render(request, 'homepage/home_aftersignin.html')
            return redirect('/home_aftersignin',{'account':temp_var[0]})
            #return redirect('/home_aftersignin')
        else:
            return HttpResponse("<h2>The email address or password you entered is wrong </h2>")
# def profile(request):
#     if request.method == 'POST':
#         temp_email = request.POST.get('UIUC Email Address')
#         temp_password = request.POST.get('Password')
#         with connection.cursor() as cursor:
#             cursor.execute("select PassWord from signup_students where EmailAddress  = %s;", (temp_email,))
#             data = cursor.fetchone()
#             print(data)
#         if data[0] == temp_password:
#             with connection.cursor() as cursor:
#                 cursor.execute("select EmailAddress from signup_students where EmailAddress = %s", (temp_email,))
#                 row = cursor.fetchone()
#                 print(row[0])
#         return HttpResponse("<h2> Welcome back </h2>")
# def fetchlogdata(request):
#     if request.method == 'POST':
#         temp_email = request.POST.get('UIUC Email Address')
#         temp_password = request.POST.get('Password')
#         temp = [temp_email, temp_password]
#         return temp
#
# def login(request):
#     with connection.cursor() as cursor:
#         cursor.execute("select PassWord from signup_students where EmailAddress  = %s;", (fetchlogdata(request)[0],))
#         data = cursor.fetchone()
#         print(data)
#     if fetchlogdata(request)[1] == data[0]:
#         with connection.cursor() as cursor:
#             cursor.execute("select EmailAddress from signup_students where EmailAddress = %s", (fetchlogdata(request)[0],))
#             row = cursor.fetchone()
#             print(row[0])
#             return redirect('/home_aftersignin', {'account': row[0]})
#     else:
#         return HttpResponse("<h2>The email address or password you entered is wrong </h2>")
def gotoprofile(request):
    course_list = hasTaken.objects.all()
    return render(request, 'myprofile/myprofile.html', {'account': temp_var[0], 'course_list': course_list})
    #return HttpResponse("<h2>welcome back <li>{%s}</li></h2>" % temp_var)

def logoff(request):
    temp_var[0] = [" "]
    return HttpResponse("<h2>You are successfully log out</h2>")

def addCourse(request, course_id):
    courseId = course_id
    course = Courses.objects.get(id = courseId)
    temp_num = course.CourseNum
    tempName = course.CourseName
    temp_email = temp_var
    temp_course = hasTaken(EmailAddress=temp_email, CourseNum = temp_num, CourseName = tempName)
    temp_course.save()
    return HttpResponse("<h2> This course is added to your profile</h2>")

def deleteCourse(request, course_id):
    courseId = course_id
    hasTaken.objects.filter(id = courseId).delete()
    return HttpResponseRedirect(reverse('Signin:gotoprofile'))