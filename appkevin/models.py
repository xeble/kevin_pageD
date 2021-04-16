from django.db import models

# Create your models here.

class Modalidade(models.Model):

    Modalidad = models.CharField(max_length=300, null =True)
    
    def __str__(self):
        return self.Modalidad


class Clientes(models.Model):
    Nombre_y_Apellido= models.CharField(max_length=20, null =True)
    Email = models.EmailField(max_length = 254, null = True)
    Telefono = models.CharField(max_length=20, null =True)
    Mensaje = models.CharField(max_length=300, null =True)
    Atendido = models.BooleanField("Atendido", default=False)
    modalidad = models.ForeignKey(Modalidade, on_delete=models.CASCADE, null=True)

    def __str__(self):
     return self.Nombre_y_Apellido