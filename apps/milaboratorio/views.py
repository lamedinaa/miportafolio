from django.shortcuts import render
from django.http import HttpResponse
from .models import problema,solucion

def challenges(request):
    problemas = problema.objects.all()
    return render(request,'milaboratorio/milaboratorio.html',{"problemas": problemas} )


def soluciones(request,id_problem = None):
    problema_obj= problema.objects.get(id_problema = id_problem)
    solucion_obj= solucion.objects.filter(problema = problema_obj).first()
    print("objeto: {0}, type: {1}".format(problema_obj,type(problema_obj)))
    print("objeto: {0}, type: {1}".format(solucion_obj,type(solucion_obj) ) )
        
    return render(request,'milaboratorio/soluciones.html',{"problema":problema_obj,"solucion":solucion_obj })







