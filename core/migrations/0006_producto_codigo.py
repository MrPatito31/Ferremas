# Generated by Django 5.0.4 on 2024-05-30 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_remove_itemcarrito_carrito_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='codigo',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]