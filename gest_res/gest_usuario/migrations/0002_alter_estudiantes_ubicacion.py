# Generated by Django 4.0.3 on 2022-03-06 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gest_usuario', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiantes',
            name='ubicacion',
            field=models.PositiveSmallIntegerField(blank=True, db_column='Ubicacion', null=True),
        ),
    ]