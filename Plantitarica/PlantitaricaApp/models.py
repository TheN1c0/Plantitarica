from django.db import models

# Create your models here.
class Plantas(models.Model):
    id_planta  = models.AutoField(db_column='idPlanta', primary_key=True) 
    nombre = models.CharField(max_length=30)
    precio     = models.IntegerField(blank=False, null=False)
    foto = models.ImageField(upload_to='Plantas/',null=True, blank=True,verbose_name='Foto de la planta')

    def __str__(self):
        return str(self.nombre)
    
class Maceteros(models.Model):
    id_Macetero = models.AutoField(db_column='idMacetero', primary_key=True) 
    nombre = models.CharField(max_length=30)
    precio     = models.IntegerField(blank=False, null=False)
    descripcion = models.CharField(max_length=500, blank=False, null=False)
    foto = models.ImageField(upload_to='Maceteros/',null=True, blank=True,verbose_name='Foto del Macetero')

    def __str__(self):
        return str(self.nombre)
    
class Insumos(models.Model):
    id_Insumo  = models.AutoField(db_column='idInsumo', primary_key=True) 
    nombre = models.CharField(max_length=30)
    precio     = models.IntegerField(blank=False, null=False)
    descripcion = models.CharField(max_length=500, blank=False, null=False)
    foto = models.ImageField(upload_to='Insumos/',null=True, blank=True,verbose_name='Foto del Insumo')

    def __str__(self):
        return str(self.nombre)



class Clientes(models.Model):
    id_Cliente  = models.AutoField(db_column='id_Cliente', primary_key=True) 
    nombre = models.CharField(max_length=30)
    email = models.EmailField()
    contrasena = models.CharField(max_length=30)
    numero = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.nombre)