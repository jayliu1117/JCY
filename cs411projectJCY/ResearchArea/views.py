from django.shortcuts import render
from django.db import connection
# Create your views here.
def index(request):
    return render(request, 'ResearchArea/areatable.html')
def count_regis(request):
    with connection.cursor() as cursor:
        cursor.execute("select count(EmailAddress) from signup_students")
        row = cursor.fetchone()
    return render(request,'myprofile/count-reg.html', {'num_student': row[0]})