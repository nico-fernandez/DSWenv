#!/usr/bin/env python
"""
Script de prueba para verificar la nueva funcionalidad de listado de cursos
"""
import os
import sys
import django
from datetime import date, timedelta

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DDSproject.settings')
django.setup()

from DDSproject.models import Tema, Docente, Alumno, Curso

def crear_datos_prueba():
    """Crear datos de prueba para verificar la funcionalidad"""
    
    # Crear múltiples temas
    temas = [
        {
            'nombre': "Programación Python",
            'descripcion': 'Curso de programación en Python'
        },
        {
            'nombre': "Desarrollo Web",
            'descripcion': 'HTML, CSS y JavaScript'
        },
        {
            'nombre': "Base de Datos",
            'descripcion': 'SQL y administración de bases de datos'
        },
        {
            'nombre': "Machine Learning",
            'descripcion': 'Inteligencia artificial y aprendizaje automático'
        },
        {
            'nombre': "Desarrollo Móvil",
            'descripcion': 'Desarrollo de aplicaciones móviles'
        }
    ]
    
    temas_creados = []
    for tema_data in temas:
        tema, created = Tema.objects.get_or_create(
            nombre=tema_data['nombre'],
            defaults={'descripcion': tema_data['descripcion']}
        )
        temas_creados.append(tema)
        if created:
            print(f"Tema creado: {tema}")
    
    # Crear múltiples docentes
    docentes_data = [
        {
            'legajo': 12345,
            'nombre': 'Juan',
            'apellido': 'Pérez',
            'costo_semanal': 5000
        },
        {
            'legajo': 12346,
            'nombre': 'Ana',
            'apellido': 'González',
            'costo_semanal': 6000
        },
        {
            'legajo': 12347,
            'nombre': 'Carlos',
            'apellido': 'Rodríguez',
            'costo_semanal': 4500
        },
        {
            'legajo': 12348,
            'nombre': 'Laura',
            'apellido': 'Martínez',
            'costo_semanal': 5500
        },
        {
            'legajo': 12349,
            'nombre': 'Miguel',
            'apellido': 'López',
            'costo_semanal': 4800
        }
    ]
    
    docentes_creados = []
    for docente_data in docentes_data:
        docente, created = Docente.objects.get_or_create(
            legajo=docente_data['legajo'],
            defaults={
                'nombre': docente_data['nombre'],
                'apellido': docente_data['apellido'],
                'costo_semanal': docente_data['costo_semanal']
            }
        )
        if not created:
            # Actualizar costo semanal si ya existe
            docente.costo_semanal = docente_data['costo_semanal']
            docente.save()
        docentes_creados.append(docente)
        if created:
            print(f"Docente creado: {docente}")
        else:
            print(f"Docente actualizado: {docente}")
    
    # Crear múltiples alumnos
    alumnos_data = [
        {
            'legajo': 67890,
            'nombre': 'María',
            'apellido': 'García',
            'fechaNacimiento': date(2000, 1, 1),
            'direccion': 'Calle Principal 123',
            'telefono': '123456789',
            'email': 'maria@example.com'
        },
        {
            'legajo': 67891,
            'nombre': 'Pedro',
            'apellido': 'Fernández',
            'fechaNacimiento': date(1998, 5, 15),
            'direccion': 'Av. Libertad 456',
            'telefono': '987654321',
            'email': 'pedro@example.com'
        },
        {
            'legajo': 67892,
            'nombre': 'Sofía',
            'apellido': 'Hernández',
            'fechaNacimiento': date(2001, 8, 22),
            'direccion': 'Calle San Martín 789',
            'telefono': '555123456',
            'email': 'sofia@example.com'
        },
        {
            'legajo': 67893,
            'nombre': 'Diego',
            'apellido': 'Torres',
            'fechaNacimiento': date(1999, 3, 10),
            'direccion': 'Ruta 9 Km 15',
            'telefono': '444789123',
            'email': 'diego@example.com'
        },
        {
            'legajo': 67894,
            'nombre': 'Valentina',
            'apellido': 'Silva',
            'fechaNacimiento': date(2002, 11, 5),
            'direccion': 'Boulevard Central 321',
            'telefono': '333456789',
            'email': 'valentina@example.com'
        },
        {
            'legajo': 67895,
            'nombre': 'Lucas',
            'apellido': 'Morales',
            'fechaNacimiento': date(1997, 7, 18),
            'direccion': 'Calle del Sol 654',
            'telefono': '222987654',
            'email': 'lucas@example.com'
        },
        {
            'legajo': 67896,
            'nombre': 'Camila',
            'apellido': 'Reyes',
            'fechaNacimiento': date(2000, 12, 25),
            'direccion': 'Av. Independencia 987',
            'telefono': '111654321',
            'email': 'camila@example.com'
        },
        {
            'legajo': 67897,
            'nombre': 'Andrés',
            'apellido': 'Castro',
            'fechaNacimiento': date(1996, 4, 30),
            'direccion': 'Calle Belgrano 147',
            'telefono': '999321654',
            'email': 'andres@example.com'
        }
    ]
    
    alumnos_creados = []
    for alumno_data in alumnos_data:
        alumno, created = Alumno.objects.get_or_create(
            legajo=alumno_data['legajo'],
            defaults=alumno_data
        )
        alumnos_creados.append(alumno)
        if created:
            print(f"Alumno creado: {alumno}")
    
    # Crear múltiples cursos
    cursos_data = [
        {
            'nombre': "Python Básico",
            'descripcion': 'Curso introductorio a Python',
            'tema': temas_creados[0],  # Programación Python
            'docente': docentes_creados[0],  # Juan Pérez
            'precio': 15000,
            'duracion_dias': 21
        },
        {
            'nombre': "Python Avanzado",
            'descripcion': 'Programación avanzada en Python',
            'tema': temas_creados[0],  # Programación Python
            'docente': docentes_creados[1],  # Ana González
            'precio': 20000,
            'duracion_dias': 28
        },
        {
            'nombre': "Desarrollo Web Frontend",
            'descripcion': 'HTML, CSS y JavaScript moderno',
            'tema': temas_creados[1],  # Desarrollo Web
            'docente': docentes_creados[2],  # Carlos Rodríguez
            'precio': 18000,
            'duracion_dias': 24
        },
        {
            'nombre': "Desarrollo Web Backend",
            'descripcion': 'Node.js y Express',
            'tema': temas_creados[1],  # Desarrollo Web
            'docente': docentes_creados[3],  # Laura Martínez
            'precio': 22000,
            'duracion_dias': 30
        },
        {
            'nombre': "SQL Básico",
            'descripcion': 'Introducción a bases de datos SQL',
            'tema': temas_creados[2],  # Base de Datos
            'docente': docentes_creados[4],  # Miguel López
            'precio': 12000,
            'duracion_dias': 18
        },
        {
            'nombre': "Machine Learning Intro",
            'descripcion': 'Fundamentos de machine learning',
            'tema': temas_creados[3],  # Machine Learning
            'docente': docentes_creados[0],  # Juan Pérez
            'precio': 25000,
            'duracion_dias': 35
        },
        {
            'nombre': "Desarrollo Android",
            'descripcion': 'Aplicaciones móviles con Android',
            'tema': temas_creados[4],  # Desarrollo Móvil
            'docente': docentes_creados[1],  # Ana González
            'precio': 28000,
            'duracion_dias': 42
        },
        {
            'nombre': "Desarrollo iOS",
            'descripcion': 'Aplicaciones móviles con Swift',
            'tema': temas_creados[4],  # Desarrollo Móvil
            'docente': docentes_creados[3],  # Laura Martínez
            'precio': 30000,
            'duracion_dias': 45
        }
    ]
    
    cursos_creados = []
    fecha_base = date.today()
    
    for i, curso_data in enumerate(cursos_data):
        fecha_inicio = fecha_base + timedelta(days=i * 7)  # Cada curso empieza una semana después
        fecha_fin = fecha_inicio + timedelta(days=curso_data['duracion_dias'])
        
        curso, created = Curso.objects.get_or_create(
            nombre=curso_data['nombre'],
            defaults={
                'descripcion': curso_data['descripcion'],
                'tema': curso_data['tema'],
                'fechaInicio': fecha_inicio,
                'fechaFin': fecha_fin,
                'docente': curso_data['docente'],
                'precio': curso_data['precio']
            }
        )
        cursos_creados.append(curso)
        if created:
            print(f"Curso creado: {curso}")
    
    # Asignar alumnos a los cursos (distribuir aleatoriamente)
    import random
    for curso in cursos_creados:
        # Asignar entre 2 y 5 alumnos por curso
        num_alumnos = random.randint(2, 5)
        alumnos_curso = random.sample(alumnos_creados, min(num_alumnos, len(alumnos_creados)))
        curso.alumnos.set(alumnos_curso)
        print(f"Curso '{curso.nombre}' tiene {len(alumnos_curso)} alumnos")
    
    return temas_creados, docentes_creados, alumnos_creados, cursos_creados

def mostrar_calculos(curso):
    """Mostrar los cálculos realizados para el curso"""
    print("\n=== CÁLCULOS DEL CURSO ===")
    print(f"Nombre del curso: {curso.nombre}")
    print(f"Fecha inicio: {curso.fechaInicio}")
    print(f"Fecha fin: {curso.fechaFin}")
    print(f"Docente: {curso.docente.nombre} {curso.docente.apellido}")
    print(f"Costo semanal del docente: ${curso.docente.costo_semanal}")
    print(f"Precio del curso: ${curso.precio}")
    
    # Calcular semanas completas
    delta = curso.fechaFin - curso.fechaInicio
    dias_totales = delta.days
    semanas_completas = dias_totales // 7
    
    print(f"Días totales: {dias_totales}")
    print(f"Semanas completas: {semanas_completas}")
    
    # Calcular costo total
    costo_total = semanas_completas * curso.docente.costo_semanal
    print(f"Costo total: ${costo_total}")
    
    # Calcular ganancia
    ganancia = curso.precio - costo_total
    print(f"Ganancia: ${ganancia}")
    
    # Cantidad de alumnos
    cantidad_alumnos = curso.alumnos.count()
    print(f"Cantidad de alumnos: {cantidad_alumnos}")

if __name__ == "__main__":
    print("Creando datos de prueba...")
    temas, docentes, alumnos, cursos = crear_datos_prueba()
    
    print("\n=== RESUMEN DE DATOS CREADOS ===")
    print(f"Temas creados: {len(temas)}")
    for tema in temas:
        print(f"  - {tema.nombre}")
    
    print(f"\nDocentes creados: {len(docentes)}")
    for docente in docentes:
        print(f"  - {docente.nombre} {docente.apellido} (Legajo: {docente.legajo}, Costo: ${docente.costo_semanal})")
    
    print(f"\nAlumnos creados: {len(alumnos)}")
    for alumno in alumnos:
        print(f"  - {alumno.nombre} {alumno.apellido} (Legajo: {alumno.legajo})")
    
    print(f"\nCursos creados: {len(cursos)}")
    for curso in cursos:
        print(f"  - {curso.nombre} (Tema: {curso.tema.nombre}, Docente: {curso.docente.nombre} {curso.docente.apellido})")
    
    print("\n=== CÁLCULOS DETALLADOS ===")
    for curso in cursos:
        mostrar_calculos(curso)
        print("-" * 50)
    
    print("\n=== PRUEBA COMPLETADA ===")
    print("Ahora puedes probar la API en:")
    print("http://localhost:8000/api/cursos/listado_detallado/")
    print("\nPara filtrar por tema específico:")
    for i, tema in enumerate(temas, 1):
        print(f"http://localhost:8000/api/cursos/listado_detallado/?tema_id={i}")
    
    print(f"\nTotal de datos creados:")
    print(f"- {len(temas)} temas")
    print(f"- {len(docentes)} docentes") 
    print(f"- {len(alumnos)} alumnos")
    print(f"- {len(cursos)} cursos") 