import random

from django.contrib import messages, auth

from django.contrib.auth.decorators import login_required

from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.

from .models import Post, People, Comments, Profile
from .forms.forms import UpdateUserForm, UpdateProfileForm


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


@login_required
def profile_page(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='users-profile')
        else:
            user_form = UpdateUserForm(instance=request.user)
            profile_form = UpdateProfileForm(instance=request.user.profile)

        return render(request, 'profile_page.html', {'user_form': user_form, 'profile_form': profile_form})
    return render(request, 'profile_page.html')


def posts_page(request):
    return render(request, 'posts_page.html', {'posts': Post.objects.all(), 'username': auth.get_user(request).username})


# def post_page(request, publication_app_post_id=1):
#     context = {'post': Post.objects.get(id=publication_app_post_id), 'comments': Comments.objects.filter(comments_post_id=publication_app_post_id)}
#     return render(request, 'post_page.html', context)


