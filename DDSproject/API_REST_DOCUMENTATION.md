# API REST - Documentación Completa

## Base URL
```
http://127.0.0.1:8000/api/
```

---

## 📚 TEMAS

### Listar todos los temas
```http
GET /api/temas/
```

**Respuesta:**
```json
[
    {
        "id": 1,
        "nombre": "Programación Python",
        "descripcion": "Curso introductorio a Python"
    },
    {
        "id": 2,
        "nombre": "Django Framework",
        "descripcion": "Desarrollo web con Django"
    }
]
```

### Obtener tema específico
```http
GET /api/temas/1/
```

**Respuesta:**
```json
{
    "id": 1,
    "nombre": "Programación Python",
    "descripcion": "Curso introductorio a Python"
}
```

### Crear nuevo tema
```http
POST /api/temas/
Content-Type: application/json
```

**Body:**
```json
{
    "nombre": "Machine Learning",
    "descripcion": "Introducción al aprendizaje automático"
}
```

### Actualizar tema
```http
PUT /api/temas/1/
Content-Type: application/json
```

**Body:**
```json
{
    "nombre": "Python Avanzado",
    "descripcion": "Curso avanzado de Python con mejores prácticas"
}
```

### Eliminar tema
```http
DELETE /api/temas/1/
```

---

## 👨‍🏫 DOCENTES

### Listar todos los docentes
```http
GET /api/docentes/
```

**Respuesta:**
```json
[
    {
        "id": 1,
        "legajo": 12345,
        "nombre": "Juan",
        "apellido": "Pérez",
        "costo_semanal": 5000
    },
    {
        "id": 2,
        "legajo": 12346,
        "nombre": "Ana",
        "apellido": "González",
        "costo_semanal": 6000
    }
]
```

### Filtrar docentes por legajo
```http
GET /api/docentes/?legajo=12345
```

### Filtrar docentes por nombre
```http
GET /api/docentes/?nombre=Juan
```

### Filtrar docentes por apellido
```http
GET /api/docentes/?apellido=Pérez
```

### Filtrar docentes por costo semanal
```http
GET /api/docentes/?costo_semanal=5000
```

### Obtener docente específico
```http
GET /api/docentes/1/
```

**Respuesta:**
```json
{
    "id": 1,
    "legajo": 12345,
    "nombre": "Juan",
    "apellido": "Pérez",
    "costo_semanal": 5000
}
```

### Crear nuevo docente
```http
POST /api/docentes/
Content-Type: application/json
```

**Body:**
```json
{
    "legajo": 12347,
    "nombre": "Carlos",
    "apellido": "Rodríguez",
    "costo_semanal": 4500
}
```

### Actualizar docente
```http
PUT /api/docentes/1/
Content-Type: application/json
```

**Body:**
```json
{
    "legajo": 12345,
    "nombre": "Juan Carlos",
    "apellido": "Pérez López",
    "costo_semanal": 5500
}
```

### Eliminar docente
```http
DELETE /api/docentes/1/
```

---

## 👨‍🎓 ALUMNOS

### Listar todos los alumnos
```http
GET /api/alumnos/
```

**Respuesta:**
```json
[
    {
        "id": 1,
        "legajo": 1001,
        "nombre": "María",
        "apellido": "García",
        "fechaNacimiento": "1995-03-15",
        "direccion": "Av. Corrientes 1234",
        "telefono": "11-1234-5678",
        "email": "maria.garcia@email.com"
    },
    {
        "id": 2,
        "legajo": 1002,
        "nombre": "Pedro",
        "apellido": "López",
        "fechaNacimiento": "1998-07-22",
        "direccion": "Belgrano 567",
        "telefono": "11-9876-5432",
        "email": "pedro.lopez@email.com"
    }
]
```

### Filtrar alumnos por legajo
```http
GET /api/alumnos/?legajo=1001
```

### Filtrar alumnos por nombre
```http
GET /api/alumnos/?nombre=María
```

### Filtrar alumnos por apellido
```http
GET /api/alumnos/?apellido=García
```

### Obtener alumno específico
```http
GET /api/alumnos/1/
```

**Respuesta:**
```json
{
    "id": 1,
    "legajo": 1001,
    "nombre": "María",
    "apellido": "García",
    "fechaNacimiento": "1995-03-15",
    "direccion": "Av. Corrientes 1234",
    "telefono": "11-1234-5678",
    "email": "maria.garcia@email.com"
}
```

### Crear nuevo alumno
```http
POST /api/alumnos/
Content-Type: application/json
```

**Body:**
```json
{
    "legajo": 1003,
    "nombre": "Laura",
    "apellido": "Martínez",
    "fechaNacimiento": "1997-11-08",
    "direccion": "San Martín 890",
    "telefono": "11-5555-1234",
    "email": "laura.martinez@email.com"
}
```

### Actualizar alumno
```http
PUT /api/alumnos/1/
Content-Type: application/json
```

**Body:**
```json
{
    "legajo": 1001,
    "nombre": "María Elena",
    "apellido": "García López",
    "fechaNacimiento": "1995-03-15",
    "direccion": "Av. Corrientes 1234, Piso 3",
    "telefono": "11-1234-5678",
    "email": "maria.garcia@email.com"
}
```

### Eliminar alumno
```http
DELETE /api/alumnos/1/
```

---

## 📖 CURSOS

### Listar todos los cursos
```http
GET /api/cursos/
```

**Respuesta:**
```json
[
    {
        "id": 1,
        "nombre": "Python Básico",
        "descripcion": "Introducción a la programación con Python",
        "tema": {
            "id": 1,
            "nombre": "Programación Python",
            "descripcion": "Curso introductorio a Python"
        },
        "tema_id": 1,
        "fechaInicio": "2024-01-15",
        "fechaFin": "2024-03-15",
        "docente": {
            "id": 1,
            "legajo": 12345,
            "nombre": "Juan",
            "apellido": "Pérez",
            "costo_semanal": 5000
        },
        "docente_id": 1,
        "precio": 15000,
        "alumnos": [
            {
                "id": 1,
                "legajo": 1001,
                "nombre": "María",
                "apellido": "García",
                "fechaNacimiento": "1995-03-15",
                "direccion": "Av. Corrientes 1234",
                "telefono": "11-1234-5678",
                "email": "maria.garcia@email.com"
            }
        ],
        "alumnos_id": [1]
    }
]
```

### Obtener curso específico
```http
GET /api/cursos/1/
```

### Crear nuevo curso
```http
POST /api/cursos/
Content-Type: application/json
```

**Body:**
```json
{
    "nombre": "Django Web Development",
    "descripcion": "Desarrollo de aplicaciones web con Django",
    "tema_id": 2,
    "fechaInicio": "2024-02-01",
    "fechaFin": "2024-04-01",
    "docente_id": 2,
    "precio": 20000,
    "alumnos_id": [1, 2]
}
```

### Actualizar curso
```http
PUT /api/cursos/1/
Content-Type: application/json
```

**Body:**
```json
{
    "nombre": "Python Avanzado",
    "descripcion": "Curso avanzado de Python con mejores prácticas",
    "tema_id": 1,
    "fechaInicio": "2024-01-15",
    "fechaFin": "2024-03-15",
    "docente_id": 1,
    "precio": 18000,
    "alumnos_id": [1, 2, 3]
}
```

### Eliminar curso
```http
DELETE /api/cursos/1/
```

---

## 📊 LISTADO DETALLADO DE CURSOS

### Listar cursos con información detallada
```http
GET /api/cursos/listado_detallado/
```

**Respuesta:**
```json
{
    "cursos": [
        {
            "id": 1,
            "nombre": "Python Básico",
            "tema": "Programación Python",
            "fechaInicio": "2024-01-15",
            "fechaFin": "2024-03-15",
            "docente": "Juan",
            "docente_apellido": "Pérez",
            "costo_semanal": 5000,
            "costo_total": 40000,
            "ganancia": -25000,
            "cantidad_alumnos": 1
        },
        {
            "id": 2,
            "nombre": "Django Web Development",
            "tema": "Django Framework",
            "fechaInicio": "2024-02-01",
            "fechaFin": "2024-04-01",
            "docente": "Ana",
            "docente_apellido": "González",
            "costo_semanal": 6000,
            "costo_total": 48000,
            "ganancia": -28000,
            "cantidad_alumnos": 2
        }
    ],
    "total_cursos": 2
}
```

### Filtrar cursos por tema
```http
GET /api/cursos/listado_detallado/?tema_id=1
```

**Respuesta:**
```json
{
    "cursos": [
        {
            "id": 1,
            "nombre": "Python Básico",
            "tema": "Programación Python",
            "fechaInicio": "2024-01-15",
            "fechaFin": "2024-03-15",
            "docente": "Juan",
            "docente_apellido": "Pérez",
            "costo_semanal": 5000,
            "costo_total": 40000,
            "ganancia": -25000,
            "cantidad_alumnos": 1
        }
    ],
    "total_cursos": 1
}
```

---

## 👥 CLIENTES

### Listar todos los clientes
```http
GET /api/clients/
```

**Respuesta:**
```json
[
    {
        "id": 1,
        "name": "Empresa ABC",
        "email": "contacto@empresaabc.com",
        "phone": "11-1234-5678",
        "address": "Av. 9 de Julio 1234",
        "city": "Buenos Aires",
        "state": "Buenos Aires",
        "zip": "1001",
        "country": "Argentina",
        "created_at": "2024-01-15T10:30:00Z"
    }
]
```

### Obtener cliente específico
```http
GET /api/clients/1/
```

### Crear nuevo cliente
```http
POST /api/clients/
Content-Type: application/json
```

**Body:**
```json
{
    "name": "Empresa XYZ",
    "email": "info@empresaxyz.com",
    "phone": "11-9876-5432",
    "address": "Corrientes 567",
    "city": "Buenos Aires",
    "state": "Buenos Aires",
    "zip": "1002",
    "country": "Argentina"
}
```

### Actualizar cliente
```http
PUT /api/clients/1/
Content-Type: application/json
```

**Body:**
```json
{
    "name": "Empresa ABC S.A.",
    "email": "contacto@empresaabc.com",
    "phone": "11-1234-5678",
    "address": "Av. 9 de Julio 1234, Piso 5",
    "city": "Buenos Aires",
    "state": "Buenos Aires",
    "zip": "1001",
    "country": "Argentina"
}
```

### Eliminar cliente
```http
DELETE /api/clients/1/
```

---

## 🔧 CÓDIGOS DE RESPUESTA

| Código | Descripción |
|--------|-------------|
| 200 | OK - Solicitud exitosa |
| 201 | Created - Recurso creado exitosamente |
| 400 | Bad Request - Datos inválidos |
| 404 | Not Found - Recurso no encontrado |
| 405 | Method Not Allowed - Método HTTP no permitido |
| 500 | Internal Server Error - Error del servidor |

---

## 📝 NOTAS IMPORTANTES

### Filtrado
- Los parámetros de consulta solo funcionan para operaciones GET de listado
- Para operaciones específicas (GET, PUT, DELETE) usa la URL con ID: `/api/recurso/{id}/`

### Fechas
- Las fechas deben estar en formato ISO: `YYYY-MM-DD`
- Las fechas de nacimiento son obligatorias para alumnos

### Relaciones
- Para crear/actualizar cursos, usa `tema_id`, `docente_id` y `alumnos_id`
- Los IDs de alumnos son opcionales y pueden ser una lista vacía

### Cálculos automáticos
- El listado detallado de cursos calcula automáticamente:
  - Costo total basado en semanas completas
  - Ganancia (precio - costo total)
  - Cantidad de alumnos

### Validaciones
- Los legajos de docentes y alumnos deben ser únicos
- Las fechas de fin deben ser posteriores a las fechas de inicio
- Los precios deben ser valores positivos 