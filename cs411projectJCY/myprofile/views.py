from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.
def index(request):
    return render(request, 'myprofile/myprofile.html')
def coursetale(request):
    return redirect('/home_aftersignin')
def count_reg(request):
    return render(request,'myprofile/count-reg.html')