from rest_framework import serializers
from .models import Client, Tema, Docente, Alumno, Curso
from datetime import datetime, timedelta

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'name', 'email', 'phone', 'address', 'city', 'state', 'zip', 'country', 'created_at']
        read_only_fields = ['id', 'created_at']

class TemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tema
        fields = ['id', 'nombre', 'descripcion']

class DocenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Docente
        fields = ['id', 'legajo', 'nombre', 'apellido', 'costo_semanal']

    def validate_costo_semanal(self, value):
        if value < 0:
            raise serializers.ValidationError('El costo semanal debe ser un valor positivo.')
        return value

class AlumnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumno
        fields = ['id', 'legajo', 'nombre', 'apellido', 'fechaNacimiento', 'direccion', 'telefono', 'email']

class CursoSerializer(serializers.ModelSerializer):
    tema = TemaSerializer(read_only=True)
    tema_id = serializers.PrimaryKeyRelatedField(queryset=Tema.objects.all(), source='tema', write_only=True)
    docente = DocenteSerializer(read_only=True)
    docente_id = serializers.PrimaryKeyRelatedField(queryset=Docente.objects.all(), source='docente', write_only=True)
    alumnos = AlumnoSerializer(many=True, read_only=True)
    alumnos_id = serializers.PrimaryKeyRelatedField(queryset=Alumno.objects.all(), source='alumnos', many=True, write_only=True, required=False)

    class Meta:
        model = Curso
        fields = ['id', 'nombre', 'descripcion', 'tema', 'tema_id', 'fechaInicio', 'fechaFin', 'docente', 'docente_id', 'precio', 'alumnos', 'alumnos_id']
    
    def validate(self, data):
        """Validación personalizada para las fechas"""
        fecha_inicio = data.get('fechaInicio')
        fecha_fin = data.get('fechaFin')
        precio = data.get('precio')
        
        if fecha_inicio and fecha_fin:
            if fecha_inicio >= fecha_fin:
                raise serializers.ValidationError({
                    'fechaFin': 'La fecha de fin debe ser posterior a la fecha de inicio.'
                })
        
        if precio is not None and precio < 0:
            raise serializers.ValidationError({
                'precio': 'El precio debe ser un valor positivo.'
            })
        
        return data

class CursoListadoSerializer(serializers.ModelSerializer):
    tema = serializers.CharField(source='tema.nombre')
    docente = serializers.CharField(source='docente.nombre')
    docente_apellido = serializers.CharField(source='docente.apellido')
    costo_semanal = serializers.IntegerField(source='docente.costo_semanal')
    costo_total = serializers.SerializerMethodField()
    ganancia = serializers.SerializerMethodField()
    cantidad_alumnos = serializers.SerializerMethodField()
    
    class Meta:
        model = Curso
        fields = ['id', 'nombre', 'tema', 'fechaInicio', 'fechaFin', 'docente', 'docente_apellido', 
                 'costo_semanal', 'costo_total', 'ganancia', 'cantidad_alumnos']
    
    def get_costo_total(self, obj):
        """Calcula el costo total basado en semanas completas"""
        if not obj.fechaInicio or not obj.fechaFin:
            return 0
        
        # Calcula la diferencia en días
        delta = obj.fechaFin - obj.fechaInicio
        dias_totales = delta.days
        
        # Calcula las semanas completas (7 días)
        semanas_completas = dias_totales // 7
        
        # Multiplica por el costo semanal del docente
        return semanas_completas * obj.docente.costo_semanal
    
    def get_ganancia(self, obj):
        """Calcula la ganancia (precio - costo_total)"""
        costo_total = self.get_costo_total(obj)
        return obj.precio - costo_total
    
    def get_cantidad_alumnos(self, obj):
        """Obtiene la cantidad de alumnos en el curso"""
        return obj.alumnos.count()