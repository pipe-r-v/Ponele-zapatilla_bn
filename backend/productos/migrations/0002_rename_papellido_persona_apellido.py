# Generated by Django 5.0.3 on 2024-07-01 10:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='persona',
            old_name='papellido',
            new_name='apellido',
        ),
    ]
