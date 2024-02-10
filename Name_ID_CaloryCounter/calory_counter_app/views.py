from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegisterForm, UserDetailsForm, UserActivityForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from .models import UserDetails, Exercise, UserActivity, FoodList, DailyEating


def home(request):
    if request.user.is_authenticated:
        return redirect('rendering')
    else:
        return render(request, 'index.html')


def register_view(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        user = User.objects.get(email=email)
        if user is not None:
            obj = authenticate(username=user.username, password=password)
            login(request, obj)
            return redirect('rendering')
    return render(request, 'login.html')


def rendering(request):
    try:
        obj_o = UserDetails.objects.get(author=request.user)
        try:
            obj_a = UserActivity.objects.get(user=obj_o)
            return redirect("results")
        except:
            return redirect("create_activity")
    except:
        return redirect("create_details")


def logout_view(request):
    logout(request)
    return redirect('login')


def results(request):
    c_user = get_object_or_404(User, id=request.user.id)
    if UserDetails.objects.get(author=c_user):
        obj = UserDetails.objects.get(author=c_user)
        if obj.gender == "male":
            bmr = 66.47 + (13.75 * obj.weight) + (5.003 * obj.height) - (6.755 * obj.age)

        else:
            bmr = 655.1 + (9.563 * obj.weight) + (1.850 * obj.height) - (4.676 * obj.age)

        exercises = Exercise.objects.all()
        activity = get_object_or_404(UserActivity, user=obj)

        if bmr < activity.exercise.calory:
            action = "Gain"
            res = activity.exercise.calory - bmr
        else:
            action = "Burn"
            res = bmr - activity.exercise.calory
        context = {
            'obj': obj,
            'bmr': int(bmr),
            'exercises': exercises,
            'activity': activity,
            'action': action,
            'results': int(res),
        }

        return render(request, 'results.html', context)


def user_details_create_view(request, *args):
    form = UserDetailsForm()
    if request.method == "POST":
        form = UserDetailsForm(request.POST)

        if form.is_valid():
            form2 = form.save(commit=False)
            form2.author = request.user
            form2.save()
            return redirect('create_activity')
    return render(request, 'user_details_create.html', {'form': form})


def user_activity_create_view(request):
    exercises = Exercise.objects.all()
    if request.method == "POST":
        ex_id = request.POST['ex']
        exercise = Exercise.objects.get(id=ex_id)
        user = UserDetails.objects.get(author=request.user)

        obj = UserActivity(exercise=exercise, user=user)
        obj.save()
        return redirect('results')

    return render(request, 'user_activity_create.html', {'exercises': exercises})


def gain_calories(request):
    return render(request, "gain_calories.html")


def breakfast(request):
    return render(request, 'breakfast.html')


def eat_up(request):
    return render(request, 'eat_up.html')