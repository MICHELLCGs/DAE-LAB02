from django.db import models

class Operacion(models.Model):
    num1 = models.FloatField()
    num2 = models.FloatField()
    OPERACIONES_CHOICES = [
        ('suma', 'Suma'),
        ('resta', 'Resta'),
        ('multiplicacion', 'Multiplicación'),
    ]
    operacion = models.CharField(max_length=15, choices=OPERACIONES_CHOICES)
    resultado = models.FloatField(null=True, blank=True)
