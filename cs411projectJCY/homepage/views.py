from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection

# Create your views here.
def index(request):
    return render(request, 'homepage/home.html')

def count_registrations(request):

    with connection.cursor() as cursor:
        cursor.execute("select count(id) from signup_students")
        row = cursor.fetchone()
    return render(request, 'homepage/count_registration.html',{'num_student': row[0]})

    # return HttpResponse("<h2> There are currently %s students registered!" % row[0])

def count_competitors(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        print(email)
        with connection.cursor() as cursor:
            cursor.execute("select skills from signup_students where EmailAddress = %s", [email])
            row = cursor.fetchone()
            skill = row[0]
            cursor.execute("select count(*) from (select s.EmailAddress from signup_students s inner join signup_students s1 on s.skills = s1.skills where s.id <> s1.id) b where b.EmailAddress = %s", [email])
            row = cursor.fetchone()


            return render(request, 'homepage/count_competitors_result.html', {'skill': skill, 'num_student': row[0]})
    return render(request, 'homepage/count_competitors.html')
