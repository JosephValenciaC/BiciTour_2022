# Generated by Django 4.0.5 on 2022-07-31 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registros', '0007_rename_titulo_archivos_nombre_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='archivos',
            options={'ordering': ['-created'], 'verbose_name': 'Experiencia', 'verbose_name_plural': 'Experiencias'},
        ),
        migrations.AlterField(
            model_name='tours',
            name='description',
            field=models.TextField(verbose_name='Descripción'),
        ),
    ]
