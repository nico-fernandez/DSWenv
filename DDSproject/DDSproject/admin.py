from django.contrib import admin
from .models import Client, Tema, Docente, Alumno, Curso

admin.site.register(Client)
admin.site.register(Tema)
admin.site.register(Docente)
admin.site.register(Alumno)
admin.site.register(Curso)
