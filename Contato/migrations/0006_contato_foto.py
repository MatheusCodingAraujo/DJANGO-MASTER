# Generated by Django 5.1.1 on 2024-10-01 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Contato', '0005_rename_categoriaid_contato_categoria_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contato',
            name='Foto',
            field=models.ImageField(blank=True, null=True, upload_to='Contato/'),
        ),
    ]
