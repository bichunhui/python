from django.shortcuts import render
from models import HeroInfo


def index(request):
    hero = HeroInfo()
    context = {"hero": hero}
    return render(request, 'booktest/index.html', context)


def digital(request, b, a, c):
    dlist = [b, a, c]
    empty = []
    context = {"list": dlist}
    return render(request, 'booktest/digital.html', context)


def include(request):
    context = {}
    return render(request, 'booktest/include.html', context)


def reverse(request):
    context = {}
    return render(request, 'booktest/reverse.html', context)


def base(request):
    return render(request, 'booktest/base.html')


def child(request):
    return render(request, 'booktest/child.html')


def base_goods(request):
    return render(request, 'booktest/base_goods.html')


def base_user(request):
    return render(request, 'booktest/base_user.html')


def content(request):
    return render(request, 'booktest/content.html')
