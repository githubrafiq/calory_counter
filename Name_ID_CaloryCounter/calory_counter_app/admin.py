from django.contrib import admin
from .models import UserDetails, Exercise, UserActivity, FoodList, DailyEating
# Register your models here.


class CounterModelAdmin(admin.ModelAdmin):
    list_display = ['author', 'age', 'gender', 'height', 'weight']


admin.site.register(UserDetails, CounterModelAdmin)


class ExerciseAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'calory']


admin.site.register(Exercise, ExerciseAdmin)


class UserActivityAdmin(admin.ModelAdmin):
    list_display = ['exercise', 'user']


admin.site.register(UserActivity, UserActivityAdmin)


class FoodListAdmin(admin.ModelAdmin):
    list_display = ['period', 'food_name', 'quantity', 'calory']


admin.site.register(FoodList, FoodListAdmin)


class DailyEatingAdmin(admin.ModelAdmin):
    list_display = ['consumer', 'foodlist', 'posted_on']


admin.site.register(DailyEating, DailyEatingAdmin)
