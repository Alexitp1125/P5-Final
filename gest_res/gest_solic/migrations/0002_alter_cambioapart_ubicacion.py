# Generated by Django 4.0.3 on 2022-03-07 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gest_solic', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cambioapart',
            name='ubicacion',
            field=models.PositiveBigIntegerField(db_column='Ubicacion'),
        ),
    ]
