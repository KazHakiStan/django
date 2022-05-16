import random

from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from .forms.registration import RegistrationForm
from .models import Post, People


def music_page(request):
    posts = Post.objects.filter(is_public=True).order_by('-created_at', '-id').all()
    #posts = ({'title': random.randint(100, 1_000_000), 'text': 'nmjisnidmfgsmfosmifsdfjisnfisn'} for _ in range(100))
    context = {'title': 'radio', 'posts': posts}

    return render(request, 'music_page.html', context)


def team_page(request):
    people = People.objects.all()

    context = {'title': 'Team', 'team': people}

    return render(request, 'team_page.html', context)


def main_page(request):
    context = {'title': 'Main', }

    return render(request, 'main_page.html', context)


def registration_page(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        'reg_form': RegistrationForm(),
    }
    return render(request, 'registration_page.html', context)


def login_page(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f'You are now logged in as {username}.')
                return redirect('/')
            else:
                messages.error(request, 'Invalid username or password')
        else:
            messages.error(request, 'Invalid username or password')
    form = AuthenticationForm()
    return render(request=request, template_name="login_page.html", context={'login_form':form})


def logout_page(request):
    logout(request)
    messages.info(request, 'You have successfully logged out.')
    return redirect('/')