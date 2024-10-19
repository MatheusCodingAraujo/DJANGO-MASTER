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
        User, on_delete=models.PROTECT, related_name='user_contato', blank=True, null=True)
    Categoria = models.ForeignKey(
        Categoria, on_delete=models.PROTECT, related_name='Categoria_id')
    Foto = models.ImageField(upload_to='Contato/', blank=True, null=True)
    Bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.Nome

class ContatoInventory(models.Model):
    contato_count = models.IntegerField()
    created_at = models.DateField(auto_now_add=True)
    User = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name='user_inventario')

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.contato_count}'