from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

# Create your views here.
from django.template.context_processors import csrf

from publication_app.forms.registration import RegistrationForm


def login_page(request):
    args = {}
    args.update(csrf(request))
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            args['login_error'] = "Пользователь не найден"
            return render(request, 'login_page.html', args)
    else:
        return render(request, 'login_page.html', args)


def logout_page(request):
    logout(request)
    return redirect('/')


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