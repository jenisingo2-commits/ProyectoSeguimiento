from django.db import models

# Create your models here.
from django.db import models

class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    # otros campos...