# Generated by Django 5.0.2 on 2024-02-08 15:16

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calory_counter_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='countermodel',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female')], default=django.utils.timezone.now, max_length=30),
            preserve_default=False,
        ),
    ]