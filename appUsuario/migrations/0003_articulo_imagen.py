# Generated by Django 4.1 on 2022-10-04 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appUsuario', '0002_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='articulo',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='imagenArticulo'),
        ),
    ]
