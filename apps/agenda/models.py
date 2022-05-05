from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Agenda(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    data_agenda = models.DateField(blank=True)
    hora_inicio = models.TimeField()
    hora_fim = models.TimeField()
    confirmacao = models.BooleanField(default=False)
