# Generated by Django 5.1.1 on 2024-10-06 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Contato', '0006_contato_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contato',
            name='CEP',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
