from django.db import models

class Propietario(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.TextField()
    telefono = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.nombre


class Mascota(models.Model):
    nombre = models.CharField(max_length=100)
    especie = models.CharField(max_length=100)
    raza = models.CharField(max_length=100)
    edad = models.IntegerField()
    propietario = models.ForeignKey('Propietario', on_delete=models.CASCADE)
    foto = models.ImageField(upload_to='fotos_mascotas/', blank=True, null=True)  # <-- Aquí


    def __str__(self):
        return self.nombre




class ConsultaMedica(models.Model):
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE)
    fecha = models.DateField()
    motivo = models.TextField()
    diagnostico = models.TextField()
    tratamiento = models.TextField()

    def __str__(self):
        return f"Consulta {self.fecha} - {self.mascota.nombre}"
