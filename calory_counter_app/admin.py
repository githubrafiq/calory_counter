from django.contrib import admin
from .models import *
# Register your models here.


class UserDetailsAdmin(admin.ModelAdmin):
    list_display = ['author', 'age', 'gender', 'height', 'weight']


admin.site.register(UserDetails, UserDetailsAdmin)


class FoodAdmin(admin.ModelAdmin):
    list_display = ['author', 'title', 'calory', 'posted_on']


admin.site.register(Food, FoodAdmin)


class ExerciseAdmin(admin.ModelAdmin):
    list_display = ['author', 'title', 'calory', 'posted_on']


admin.site.register(Exercise, ExerciseAdmin)

