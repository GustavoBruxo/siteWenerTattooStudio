from django.db import models

# Create your models here.


class Banner(models.Model):
    banner = models.ImageField(upload_to='fotos/%m/%Y/', blank=True)
    banner_ativo = models.BooleanField(default=False)
