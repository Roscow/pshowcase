# Generated by Django 3.1 on 2020-09-16 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0016_auto_20200916_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='retrato',
            field=models.ImageField(upload_to='cars'),
        ),
    ]