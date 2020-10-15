# Generated by Django 3.1 on 2020-09-16 23:56

from django.db import migrations
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0021_perfil_retrato3'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perfil',
            name='retrato2',
        ),
        migrations.RemoveField(
            model_name='perfil',
            name='retrato3',
        ),
        migrations.AlterField(
            model_name='perfil',
            name='retrato',
            field=stdimage.models.StdImageField(blank=True, null=True, upload_to='path/to/img'),
        ),
    ]