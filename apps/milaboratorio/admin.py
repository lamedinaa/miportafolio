from django.contrib import admin

# Register your models here.
from .models import problema, solucion

admin.site.register(problema)
admin.site.register(solucion)