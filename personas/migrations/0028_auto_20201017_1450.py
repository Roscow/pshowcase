# Generated by Django 3.1 on 2020-10-17 17:50

from django.db import migrations
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0027_auto_20201017_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='retrato',
            field=stdimage.models.StdImageField(blank=True, null=True, upload_to=''),
        ),
    ]
