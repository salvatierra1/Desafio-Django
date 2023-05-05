from datetime import datetime
from django import forms
from django.db import models

# Create your models here.

#Clase Cliente
class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    dni = models.PositiveIntegerField(verbose_name="D.N.I", unique=True, blank=True)
    nombre= models.CharField(verbose_name="Nombre/s", max_length=30)
    apellido=models.CharField(verbose_name="Apellido/s", max_length=30)
    ciudad=models.CharField(verbose_name="Ciudad", max_length=30)
    direccion=models.CharField(verbose_name="Direccion", max_length=30)
    fecha_alta=models.DateField(verbose_name="Fecha de alta", max_length=15, default=datetime.now(), blank=True)
    estado=models.BooleanField(verbose_name="Estado")

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    class Meta:
        db_table = "cliente"
        ordering = ["id"]
     

#Clase Tipo de Mascota
class TipoMascota(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(verbose_name="Nombre", max_length=30)

    def __str__(self):
        return f"{self.nombre}"
    
    class Meta:
        db_table = "tipo_mascota"
        ordering = ["id"]


#Clase Mascota
class Mascota(models.Model):
    id = models.AutoField(primary_key=True)
    cliente_id = models.ForeignKey(Cliente, on_delete=models.PROTECT, verbose_name= "propietario" )
    numero_chip = models.IntegerField(verbose_name="Numero de chip", unique=True, blank=True)
    nombre_mascota = models.CharField(verbose_name="Nombre de mascota", max_length=30)
    tipo_mascota = models.ForeignKey(TipoMascota, on_delete=models.PROTECT, verbose_name= "tipo de mascota" )
    estado=models.BooleanField(verbose_name="Estado")

    def __str__(self):
        return f"{self.tipo_mascota}"
    
    class Meta:
        db_table = "mascota"
        ordering = ["id"]

#Clase Historia Clinica
class HistoriaClinica(models.Model):
    id = models.AutoField(primary_key=True)
    mascota_id = models.ForeignKey(Mascota, on_delete=models.PROTECT, verbose_name= "mascota" )
    fecha_consulta=models.DateField(verbose_name="Fecha de consulta", max_length=15, default=datetime.now(), blank=True)
    observaciones = models.CharField(verbose_name= "Observaciones", max_length=500)

    def __str__(self):
        return f"{self.fecha_consulta}"
    
    class Meta:
        db_table = "historia_clinica"
        ordering = ["id"]