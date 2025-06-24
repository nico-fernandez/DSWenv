from rest_framework import viewsets
from .models import Client, Tema, Docente, Alumno, Curso
from .serializers import ClientSerializer, TemaSerializer, DocenteSerializer, AlumnoSerializer, CursoSerializer

class ClientViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gestionar los clientes.
    Proporciona operaciones CRUD completas.
    """
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class TemaViewSet(viewsets.ModelViewSet):
    queryset = Tema.objects.all()
    serializer_class = TemaSerializer

class DocenteViewSet(viewsets.ModelViewSet):
    queryset = Docente.objects.all()
    serializer_class = DocenteSerializer

class AlumnoViewSet(viewsets.ModelViewSet):
    queryset = Alumno.objects.all()
    serializer_class = AlumnoSerializer

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer 