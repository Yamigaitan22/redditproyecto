# Generated by Django 4.0.3 on 2022-03-15 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Noticias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('encabezado', models.CharField(max_length=100)),
                ('describcion', models.TextField()),
                ('autor', models.CharField(max_length=100)),
                ('fecha', models.CharField(max_length=100)),
            ],
        ),
    ]
