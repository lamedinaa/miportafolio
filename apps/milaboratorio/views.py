from django.shortcuts import render
from django.http import HttpResponse


def challenges(request):
    return render(request,'milaboratorio/milaboratorio.html')







