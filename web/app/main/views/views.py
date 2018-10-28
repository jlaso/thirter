from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def home(request):
    # check if user is already logged in
    if 'user' in request.session:
        return go_home(request)

    return render(request, 'home.html')


def login(request):
    if request.method == 'POST':
        return do_login(request)

    # check if user is already logged in
    if 'user' in request.session:
        return go_home(request)

    return render(request, 'login.html')


def do_logout(request):
    if 'user' in request.session:
        del request.session['user']
    logout(request)

    return redirect(settings.HOME_ABS_PATH)


def do_login(request):
    user_name = request.POST.get('_username')
    user_password = request.POST.get('_password')
    user = authenticate(request, username=user_name, password=user_password)
    if user is None:
        messages.add_message(request, messages.ERROR, 'Bad user-password combination')
        return render(request, 'home.html')

    login(request, user)
    request.session['user'] = user_name

    return go_home(request)


def go_home(request):
    user = request.user
    if not user.is_authenticated:
        return redirect('main:home')
    return redirect('main:dashboard')
