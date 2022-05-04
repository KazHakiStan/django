import random

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
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
