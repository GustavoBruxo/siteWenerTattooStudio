from django.db import models

# Create your models here.


class Tattoo(models.Model):
    nome_tattoo = models.CharField(max_length=100)
    foto_tattoo = models.ImageField(upload_to='fotos/%m/%Y/', blank=True)
    data_inclusao = models.DateTimeField()
    destaque = models.BooleanField(default=True)

    def __str__(self):
        return self.nome_tattoo
    

class Piercings(models.Model):
    nome_piercings = models.CharField(max_length=100)
    foto_piercings = models.ImageField(upload_to='fotos/%m/%Y/', blank=True)
    data_inclusao = models.DateTimeField()
    destaque = models.BooleanField(default=True)

    def __str__(self):
        return self.nome_piercings
