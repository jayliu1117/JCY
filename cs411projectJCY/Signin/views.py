from django.shortcuts import render
# from django.http import HttpResponse
# from django.db import connection
# from ..Signup.models import Students

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
