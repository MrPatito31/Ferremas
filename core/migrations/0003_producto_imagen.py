# Generated by Django 5.0.4 on 2024-05-28 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_producto_categoria_delete_categoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='imagen',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
