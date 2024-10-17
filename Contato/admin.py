from django.contrib import admin
from Contato.models import Contato, Categoria

# Register your models here.


class ContatoAdmin(admin.ModelAdmin):
    list_display = ('Nome', 'Email', 'Telefone', 'DataNascimento')
    search_fields = ('Nome', 'Email')


admin.site.register(Contato, ContatoAdmin)


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('Categoria',)
    search_fields = ('Categoria',)


admin.site.register(Categoria, CategoriaAdmin)
