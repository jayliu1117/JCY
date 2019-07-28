from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'ResearchArea/areatable.html')
def count_regis(request):
    return render(request,'myprofile/count-reg.html')