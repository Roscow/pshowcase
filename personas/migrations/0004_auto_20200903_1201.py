# Generated by Django 3.1 on 2020-09-03 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0003_auto_20200901_2342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='correo',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
