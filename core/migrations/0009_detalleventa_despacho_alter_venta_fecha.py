# Generated by Django 5.0.4 on 2024-05-30 04:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_venta_detalleventa'),
    ]

    operations = [
        migrations.AddField(
            model_name='detalleventa',
            name='despacho',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='venta',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 30, 0, 53, 47, 919639)),
        ),
    ]
