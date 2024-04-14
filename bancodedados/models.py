from django.db import models

# Create your models here.

class teste(models.Model):
    id = models.AutoField(primary_key=True)
    texto = models.CharField(max_length=20)
    
    def __str__(self) -> str:
        return self.texto
