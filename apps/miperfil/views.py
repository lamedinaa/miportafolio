from django.shortcuts import render
from django.http import HttpResponse


""" def index(request):
    return HttpResponse("Index")
 """

def index(request):
    return render(request,'miperfil/index.html')
    