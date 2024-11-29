from django.db import models

class MenuItem(models.Model):
    nome = models.CharField(max_length=100)
    ingredientes = models.TextField()
    foto = models.ImageField(upload_to='fotos_pratos/')
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nome
