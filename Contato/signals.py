from django.db.models.signals import pre_save, pre_delete, post_delete, post_save
from django.dispatch import receiver
from Contato.models import Contato, ContatoInventory
from app.middleware import get_current_user

def Contato_Inventory_Update():
    user = get_current_user()#pra fazer isso tive que criar um middleware no app principal, e configura-lo no arquivo de settings.py
    contatos_count= Contato.objects.all().count()
    #para o sum abaixo tem q importar: import django.db.models import Sum 
    #Car.objects.agregate(total_value=Sum('value'))['total_value']    deixando aqui comentado pois nao precisei no meu cenario, mas é util
    ContatoInventory.objects.create(
        contato_count=contatos_count,
        User=user
    )

@receiver(pre_delete, sender=Contato)
def contato_pre_delete(sender, instance, **kwargs):
    print('### PRE DELETE###')

@receiver(post_delete, sender=Contato)
def contato_post_delete(sender, instance, **kwargs):
    Contato_Inventory_Update()


@receiver(pre_save, sender=Contato)
def contato_pre_save(sender, instance, **kwargs):
    if not instance.Bio:
        instance.Bio='Bio gerada automaticamente'#AULA 82 ENSINA A COLOCAR IA =, não fiz pq não tenho credito 
    instance.User=get_current_user()

@receiver(post_save, sender=Contato)
def contato_post_save(sender, instance, created, **kwargs):
    if created:
        Contato_Inventory_Update()