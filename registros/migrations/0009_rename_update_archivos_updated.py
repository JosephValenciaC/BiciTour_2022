# Generated by Django 4.0.5 on 2022-08-15 02:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registros', '0008_alter_archivos_options_alter_tours_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='archivos',
            old_name='update',
            new_name='updated',
        ),
    ]