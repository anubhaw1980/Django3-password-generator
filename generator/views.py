from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def aboutus(request):
#    return HttpResponse("<h1>Hello Audience! We are Agrawal family working on the Django project</h1><br><br><h3>Anubhaw Agrawal<br>Prabhaw Agrawal</h3><br>")
    return render(request, 'generator/aboutus.html')

def home(request):
    return render(request, 'generator/home.html',{'variable_key':'VALUE TO BE DISPLAYED'})

def testres(request):
    return render(request,'generator/testresponse.html',{'variable_key':'VALUE TO BE DISPLAYED'})

def passwords(request):

    passcode=''
    passcodelen=int(request.GET.get('length',12))
    charset=list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('Uppercase'):
        charset.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('Numbers'):
        charset.extend(list('0123456789'))
    if request.GET.get('Special'):
        charset.extend(list('~!@#$%^&*()_'))
    for i in range(passcodelen):
        passcode += random.choice(charset)
    return render(request, 'generator/passwords.html', {'passcode':passcode})
