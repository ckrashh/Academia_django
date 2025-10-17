from django.db import models

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.nombre

class Perfil(models.Model):
    estudiante = models.OneToOneField(
        Estudiante,
        on_delete=models.CASCADE,   
        related_name='perfil'       
    )
    biografia = models.TextField()
    foto = models.ImageField(upload_to='imagenes/', null=True, blank=True)
    redes = models.URLField()

    def __str__(self):
        return f"Perfil de {self.estudiante.nombre}" 