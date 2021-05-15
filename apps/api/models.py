from django.db import models

# Create your models here.
MASCULINO="masculino"
FEMENINO='femenino'
GENERO_CHOICE=[
    (MASCULINO ,'masculino'),
    (FEMENINO ,'femenino')
]

class Persona(models.Model):
    name = models.CharField('Nombre', max_length=50)
    apellido = models.CharField('Apellido', max_length=50)
    Genero = models.CharField(
        'Genero', choices=GENERO_CHOICE, max_length=50)
    
    def __str__(self) :
        return self.name
