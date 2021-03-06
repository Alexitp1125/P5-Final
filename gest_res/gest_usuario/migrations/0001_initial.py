# Generated by Django 4.0.3 on 2022-03-06 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estudiantes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.TextField(blank=True, db_column='Nombres', null=True)),
                ('apellidos', models.TextField(blank=True, db_column='Apellidos', null=True)),
                ('usuario', models.TextField(blank=True, db_column='Usuario', null=True)),
                ('contrasena', models.TextField(blank=True, null=True)),
                ('categoria', models.TextField(blank=True, db_column='Categoria', null=True)),
                ('ubicacion', models.TextField(blank=True, db_column='Ubicacion', null=True)),
            ],
            options={
                'verbose_name': 'Estudiante',
                'verbose_name_plural': 'Estudiantes',
                'db_table': 'estudiantes',
                'ordering': ['id'],
            },
        ),
    ]
