# Generated by Django 3.1 on 2020-09-03 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0004_auto_20200903_1201'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='icono_categoria',
            field=models.CharField(default='direccion', max_length=200),
            preserve_default=False,
        ),
    ]