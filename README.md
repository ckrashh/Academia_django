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
pip install pymysql

# Aplicar migraciones
python manage.py makemigrations
python manage.py migrate

# Cargar datos de prueba
python manage.py shell < consultas.txt
```

## 🔍 Consultas
👨‍🎓1. Creación de Estudiantes

Se crearon cinco estudiantes con nombre y correo electrónico, para probar su inscripción en cursos y la relación uno a uno con sus perfiles.

👨‍🏫 2. Creación de Profesores

Se registraron dos profesores, quienes luego fueron asignados como responsables de distintos cursos. Esto validó la relación muchos a uno entre curso y profesor.

📘 3. Creación de Cursos

Se generaron tres cursos, cada uno asignado a un profesor específico. Esto permitió verificar la relación ForeignKey con borrado en cascada desde el profesor.

🧑‍💻 4. Creación de Perfiles

A cada estudiante se le asignó un perfil único con información adicional como biografía y enlace a redes sociales, validando la relación uno a uno (OneToOneField).

📚 5. Creación de Inscripciones

Se inscribieron estudiantes en distintos cursos. Se usó una tabla intermedia para almacenar la fecha de inscripción (automática), el estado de la inscripción (activo o finalizado) y la nota final (opcional), cumpliendo así con una relación muchos a muchos con datos adicionales.

✏️ 6. Edición de Inscripción

Se accedió a una inscripción específica (id = 3) para modificar su estado y añadir una nota final. Esto validó que los campos personalizados de la tabla intermedia son editables.

❌ 7. Borrado en Cascada

Se eliminó un perfil de estudiante y se comprobó que se elimina correctamente sin afectar otras entidades. También se probó la eliminación de un estudiante y cómo esta acción borra automáticamente su perfil y sus inscripciones asociadas gracias al uso de on_delete=models.CASCADE.

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




