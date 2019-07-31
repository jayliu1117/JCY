from django.shortcuts import render
from django.shortcuts import redirect
from django.db import connection
# Create your views here.
def index(request):
    return render(request, 'myprofile/myprofile.html')
def coursetale(request):
    return redirect('/home_aftersignin')
def count_reg(request):
    with connection.cursor() as cursor:
        cursor.execute("select count(EmailAddress) from signup_students")
        row = cursor.fetchone()
    return render(request,'myprofile/count-reg.html',{'num_student': row[0]})