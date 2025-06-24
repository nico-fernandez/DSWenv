from rest_framework import serializers
from .models import Client, Tema, Docente, Alumno, Curso

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
        fields = ['id', 'legajo', 'nombre', 'apellido']

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