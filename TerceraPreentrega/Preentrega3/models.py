from django.db import models

class ingresos(models.Model):
    
    cantidad = models.IntegerField()
class ahorros(models.Model):
    
    cantidad = models.IntegerField()
class gastos(models.Model):
    
    cantidad = models.IntegerField()