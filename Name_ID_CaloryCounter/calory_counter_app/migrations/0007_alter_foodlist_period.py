# Generated by Django 5.0.2 on 2024-02-10 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calory_counter_app', '0006_foodlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodlist',
            name='period',
            field=models.CharField(choices=[('breakfast', 'Breakfast'), ('morning_snack', 'Morning Snack'), ('lunch', 'Lunch'), ('evening_snack', 'Evening Snack'), ('dinner', 'Dinner')], max_length=30),
        ),
    ]
