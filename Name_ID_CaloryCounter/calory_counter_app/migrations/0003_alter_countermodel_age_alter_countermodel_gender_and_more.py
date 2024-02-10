# Generated by Django 5.0.2 on 2024-02-08 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calory_counter_app', '0002_countermodel_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='countermodel',
            name='age',
            field=models.IntegerField(default=25),
        ),
        migrations.AlterField(
            model_name='countermodel',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female')], default='male', max_length=30),
        ),
        migrations.AlterField(
            model_name='countermodel',
            name='height',
            field=models.IntegerField(default=180),
        ),
        migrations.AlterField(
            model_name='countermodel',
            name='weight',
            field=models.IntegerField(default=60),
        ),
    ]
