from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.


class UserDetails(models.Model):
    GENDER = (
        ('male', 'Male'),
        ('female', 'Female')
    )
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(default=25)
    gender = models.CharField(max_length=30, choices=GENDER, default='male')
    height = models.IntegerField(default=180)
    weight = models.IntegerField(default=60)

    def __str__(self):
        return self.author.username


class Exercise(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    calory = models.IntegerField()

    def __str__(self):
        return self.title


class UserActivity(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    user = models.OneToOneField(UserDetails, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.author.username


class FoodList(models.Model):
    PERIOD = (
        ('breakfast', 'Breakfast'),
        ('morning_snack', 'Morning Snack'),
        ('lunch', 'Lunch'),
        ('evening_snack', 'Evening Snack'),
        ('dinner', 'Dinner'),
    )
    period = models.CharField(max_length=30, choices=PERIOD)
    food_name = models.CharField(max_length=30)
    quantity = models.CharField(max_length=30)
    calory = models.IntegerField()

    def __str__(self):
        return self.period


class DailyEating(models.Model):
    consumer = models.ForeignKey(User, on_delete=models.CASCADE)
    foodlist = models.ForeignKey(FoodList, on_delete=models.CASCADE)
    posted_on = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.consumer.username
