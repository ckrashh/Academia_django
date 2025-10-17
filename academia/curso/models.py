from django.db import models
from django.core.validators import MaxValueValidator
from profesores.models import Profesor
from estudiantes.models import Estudiante
class Curso(models.Model):
    id_profesor = models.ForeignKey(
        Profesor, 
        on_delete=models.CASCADE,
        related_name='cursos'
    )
    id_estudiante = models.ManyToManyField(Estudiante, through='Inscripcion', related_name='Inscripciones')
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre


class Inscripcion(models.Model):
    id_estudiante = models.ForeignKey(
        Estudiante, 
        on_delete=models.CASCADE,
        related_name='inscripciones'
    )
    id_curso = models.ForeignKey(
        Curso, 
        on_delete=models.CASCADE,
        related_name='inscripciones'
    )
    fecha_inscripcion = models.DateField(auto_now_add=True)
    estado = models.CharField(
        max_length=20,
        choices=[('activo','Activo'), ('finalizado','Finalizado')],
        default='activo'
    )
    nota_final = models.DecimalField( 
        max_digits=2,
        validators=[MaxValueValidator(7.0)], 
        decimal_places=1, 
        null=True, 
        blank=True
    )

    def __str__(self):
        return f"{self.id_estudiante.nombre} - {self.id_curso.nombre} - {self.nota_final}"

