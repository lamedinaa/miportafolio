from django.db import models

# Create your models here.

class problema(models.Model):
    id_problema = models.CharField(max_length=2)
    nombre_problema = models.CharField(max_length=100)
    plataforma_problema = models.CharField(max_length=100)
    descripcion = models.TextField()
    

    def __str__(self):
        return self.nombre_problema

class solucion(models.Model):
    problema = models.OneToOneField(problema,on_delete=models.CASCADE)
    texto_solucion = models.TextField(blank = True, null = True)
    link_gist = models.CharField(max_length=100,blank=True,null = True)

    