from django.db import models
from django.contrib.auth.models import User


class Categoria(models.Model):
    ID = models.AutoField(primary_key=True)
    Categoria = models.CharField(max_length=50)

    def __str__(self):
        return self.Categoria


class Contato(models.Model):
    ID = models.AutoField(primary_key=True)
    Nome = models.CharField(max_length=250)
    Email = models.EmailField(blank=True, null=True)
    Telefone = models.CharField(max_length=20, blank=True, null=True)
    DataNascimento = models.DateField(blank=True, null=True)
    CEP = models.CharField(max_length=20, blank=True, null=True)
    User = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name='user_id')
    Categoria = models.ForeignKey(
        Categoria, on_delete=models.PROTECT, related_name='Categoria_id')
    Foto = models.ImageField(upload_to='Contato/', blank=True, null=True)

    def __str__(self):
        return self.Nome
