# Generated by Django 4.0.3 on 2022-04-22 02:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Reddit_app', '0005_comentarios'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comentarios',
            name='telefono',
        ),
    ]