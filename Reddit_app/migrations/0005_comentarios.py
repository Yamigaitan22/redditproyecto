# Generated by Django 4.0.3 on 2022-03-24 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reddit_app', '0004_delete_comentario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=150)),
                ('telefono', models.CharField(max_length=150)),
                ('comentario', models.TextField()),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
            },
        ),
    ]
