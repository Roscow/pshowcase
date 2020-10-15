# Generated by Django 3.1 on 2020-09-17 23:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('personas', '0022_auto_20200916_2056'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='user_credentials',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]