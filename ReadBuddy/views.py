from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from ReadBuddy.models import random99


def index(request):
    return render(request, 'index.html')


def hitPage2(request):
    someclass = random99()
    data=someclass.convertPdf()

    return render(request,'page2.html', {'data':data})
    #return HttpResponse(random99.math(0))