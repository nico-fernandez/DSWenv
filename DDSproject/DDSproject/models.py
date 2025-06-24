from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class Tema(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    def __str__(self):
        return self.nombre

class Docente(models.Model):
    legajo = models.BigIntegerField(unique=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    costo_semanal = models.IntegerField(default=0)
    def clean(self):
        super().clean()
        if self.costo_semanal < 0:
            raise ValidationError({'costo_semanal': _('El costo semanal debe ser un valor positivo.')})
    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.legajo})"

class Alumno(models.Model):
    legajo = models.BigIntegerField(unique=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fechaNacimiento = models.DateField()
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.legajo})"

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    tema = models.ForeignKey(Tema, on_delete=models.PROTECT)
    fechaInicio = models.DateField()
    fechaFin = models.DateField()
    docente = models.ForeignKey(Docente, on_delete=models.PROTECT)
    precio = models.FloatField()
    alumnos = models.ManyToManyField(Alumno, blank=True)
    
    def clean(self):
        """Validación personalizada para las fechas"""
        super().clean()
        if self.fechaInicio and self.fechaFin:
            if self.fechaInicio >= self.fechaFin:
                raise ValidationError({
                    'fechaFin': _('La fecha de fin debe ser posterior a la fecha de inicio.')
                })
        if self.precio < 0:
            raise ValidationError({'precio': _('El precio debe ser un valor positivo.')})
    
    def save(self, *args, **kwargs):
        """Llamar clean() antes de guardar"""
        self.full_clean()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.nombre