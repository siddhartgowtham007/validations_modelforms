from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
from app.models import *
# Create your views here.

def student1(request):
    SEFO=Studentform()
    d={'SEFO':SEFO}

    if request.method=='POST':
        SFO=Studentform(request.POST)
        if SFO.is_valid():
            SFO.save()
            return HttpResponse('inserted')
        else:
            return HttpResponse('invalid data')
    return render(request,'student.html',d)
