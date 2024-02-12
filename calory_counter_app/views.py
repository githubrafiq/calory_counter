from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .forms import RegisterForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate

from .models import UserDetails, Food, Exercise
from .forms import UserDetailsForm
from django.utils import timezone



def home(request):
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
        password = request.POST['password']
        try:
            as_username = request.POST['username_or_email']
            if as_username is not None:
                obj = authenticate(username=as_username, password=password)
                login(request, obj)
        except:
            as_email = request.POST['username_or_email']
            user = User.objects.get(email=as_email)
            if user is not None:
                obj = authenticate(username=user.username, password=password)
                login(request, obj)
        return redirect('rendering')

    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


def user_details_create_view(request, *args):
    form = UserDetailsForm()
    if request.method == "POST":
        form = UserDetailsForm(request.POST)

        if form.is_valid():
            form2 = form.save(commit=False)
            form2.author = request.user
            form2.save()
            return redirect('results')
    return render(request, 'user_details_create.html', {'form': form})


def results(request):
    c_user = get_object_or_404(User, id=request.user.id)
    try:
        obj = UserDetails.objects.get(author=c_user)
        if obj.gender == "male":
            bmr = 66.47 + (13.75 * obj.weight) + (5.003 * obj.height) - (6.755 * obj.age)

        else:
            bmr = 655.1 + (9.563 * obj.weight) + (1.850 * obj.height) - (4.676 * obj.age)

        today_date = timezone.now().date()

        if request.method == "POST":
            input_date = request.POST['date']
        else:
            input_date = today_date
        foods_on_date = Food.objects.filter(author=request.user, posted_on__date=input_date)
        exercises_on_date = Exercise.objects.filter(author=request.user, posted_on__date=input_date)

        total_consumed = 0
        foods = Food.objects.filter(author=request.user, posted_on__date=today_date)
        for food in foods:
            total_consumed += food.calory

        total_burned = 0
        exercise = Exercise.objects.filter(author=request.user, posted_on__date=today_date)
        for exercise in exercise:
            total_burned += exercise.calory

        total_consumed_on_date = 0
        for food in foods_on_date:
            total_consumed_on_date += food.calory

        total_burned_on_date = 0
        for exercise in exercises_on_date:
            total_burned_on_date += exercise.calory

        required_calory = bmr+total_burned
        balance = required_calory - total_consumed

        if balance > 0:
            suggestion = 'gain'
        else:
            suggestion = 'burn'


        context = {
            'obj': obj,
            'bmr': int(bmr),
            'foods_on_date': foods_on_date,
            'exercises_on_date': exercises_on_date,
            'input_date': input_date,
            'total_consumed': total_consumed,
            'total_burned': total_burned,
            'required_calory': required_calory,
            'balance': balance,
            'suggestion': suggestion,
            'total_consumed_on_date': total_consumed_on_date,
            'total_burned_on_date': total_burned_on_date,
        }
        return render(request, 'results.html', context)
    except:
        return redirect('rendering')


def rendering(request):
    try:
        obj_o = UserDetails.objects.get(author=request.user)
        return redirect("results")
    except:
        if request.user.is_authenticated:
            return redirect("create_details")
        else:
            return redirect('login')


def consume_calory(request):
    if request.method == "POST":
        title = request.POST.get('title')
        calory = request.POST.get('calory')

        add_item = Food(title=title, calory=calory, author=request.user)
        add_item.save()
        return redirect('results')


def burn_calory(request):
    if request.method == "POST":
        title = request.POST['title']
        calory = request.POST['calory']
        add_item = Exercise(title=title, calory=calory, author=request.user)
        add_item.save()
        return redirect('results')


def food_list_on_date(request):
    if request.method == "POST":
        date = request.POST['date']

        return redirect('results')

