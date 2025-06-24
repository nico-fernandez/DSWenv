from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Q
from .models import Client, Tema, Docente, Alumno, Curso
from .serializers import ClientSerializer, TemaSerializer, DocenteSerializer, AlumnoSerializer, CursoSerializer, CursoListadoSerializer

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
    
    @action(detail=False, methods=['get'])
    def listado_detallado(self, request):
        """
        Obtiene un listado de todos los cursos filtrado por tema obligatorio,
        con información detallada incluyendo cálculos de costos y ganancias.
        """
        # Obtener el parámetro de tema (opcional)
        tema_id = request.query_params.get('tema_id')
        
        # Filtrar cursos por tema si se especifica
        queryset = Curso.objects.all()
        if tema_id:
            queryset = queryset.filter(tema_id=tema_id)
        
        # Ordenar por fecha de inicio
        queryset = queryset.order_by('fechaInicio')
        
        # Serializar con el serializer específico para listado
        serializer = CursoListadoSerializer(queryset, many=True)
        
        return Response({
            'cursos': serializer.data,
            'total_cursos': queryset.count()
        }) 