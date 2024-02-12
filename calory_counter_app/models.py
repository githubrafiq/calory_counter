from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


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


class Food(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    calory = models.IntegerField()
    posted_on = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.title}"


class Exercise(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    calory = models.IntegerField()
    posted_on = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.title}"
