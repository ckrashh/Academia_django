# Academia_django

# 🎓 Plataforma de Gestión Académica
# M7_AE3_ABPRO-Ejercicio grupal

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

Sistema de gestión académica con Django ORM que modela relaciones entre estudiantes, profesores, cursos e inscripciones.

## 👥 Equipo

- Johana Torres
- Linwi Vargas
- Gerald Carrillo
- Matías Lagos
- Sofía Lagos

## 📊 Estructura de Datos

### Modelos y Relaciones

**Estudiante** ─ **Perfil** (OneToOne)
- Información básica y perfil extendido con biografía, foto y redes sociales

**Profesor** ─< **Curso** (ForeignKey)
- Un profesor imparte múltiples cursos

**Estudiante** >─< **Curso** (ManyToMany)
- Gestión mediante modelo intermedio `Inscripcion` con:
  - Fecha de inscripción
  - Estado (activo/finalizado)
  - Nota final (0.0 - 7.0)

## 🚀 Instalación

```bash
# Clonar y entrar al proyecto
git clone <(https://github.com/ckrashh/Academia_django)>
cd academia

# Crear entorno virtual
python -m venv venv
source venv/scripts/activate  # Windows: venv\Scripts\activate

# Instalar dependencias
pip install django pillow

# Aplicar migraciones
python manage.py makemigrations
python manage.py migrate

# Cargar datos de prueba
python manage.py shell < consultas.txt

# Ejecutar servidor
python manage.py runserver
```

## ✨ Funcionalidades

- CRUD completo de estudiantes, profesores y cursos
- Sistema de inscripciones con seguimiento de estado
- Gestión de calificaciones (escala 0.0 - 7.0)
- Perfiles de estudiante con información adicional
- Borrado en cascada automático

## 📝 Características Técnicas

- Uso de `ForeignKey`, `ManyToManyField` y `OneToOneField`
- Modelo intermedio personalizado para relaciones M2M
- Validación de notas con `MaxValueValidator`
- Campos auto-generados (`auto_now_add`)
- Borrado en cascada (`on_delete=CASCADE`)

## 📂 Estructura del Proyecto

```
academia/
├── estudiantes/
│   └── models.py (Estudiante, Perfil)
│   └── ...
├── profesores/
│   └── models.py (Profesor)
│   └── ...
├── curso/
│   └── models.py (Curso, Inscripcion)
│   └── ...
└── consultas.txt (Script de datos de prueba)
```

---

**Proyecto Académico del Modulo 7 para el Bootcamp de Desarrollo Full Stack Python** 


