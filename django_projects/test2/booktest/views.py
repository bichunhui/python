# coding=utf-8
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from models import *


def index(request):
    list = BookInfo.books2.all()
    context = {"list": list}
    return render(request, "booktest/index.html", context)


def gettest1(request):
    return render(request, "booktest/getTest1.html")


def gettest2(request):
    a1 = request.GET.get("a")
    a2 = request.GET.get("b")
    a3 = request.GET.get("c")
    context = {"a": a1, "b": a2, "c": a3}
    return render(request, "booktest/getTest2.html", context)


def gettest3(request):
    a1 = request.GET.get("a")
    a2 = request.GET.get("b")
    context = {"a": a1, "b": a2}
    return render(request, "booktest/getTest3.html", context)


def posttest1(request):
    return render(request, "booktest/postTest1.html")


def posttest2(request):
    uname = request.POST['uname']
    upwd = request.POST['upwd']
    ugender = request.POST.get('ugender')
    uhobby = request.POST.getlist('uhobby')
    context = {"uname": uname, "upwd": upwd, "ugender": ugender, "uhobby": uhobby}
    return render(request, "booktest/postTest2.html", context)


def cookietest(request):
    response = HttpResponse()
    cookie = request.COOKIES
    if "t1" in cookie:
        response.write(cookie["t1"])
    # response.set_cookie("t1","fanjiale")
    return response


def redtest1(request):
    return HttpResponseRedirect('/booktest/redTest2/')


def redtest2(request):
    return HttpResponse("这是转向来的页面！")


def session1(request):
    uname = request.session['uname']
    # uname = None
    context = {"uname": uname}
    return render(request, 'booktest/session1.html/', context)


def session2(request):
    return render(request, 'booktest/session2.html/')


def session2_handle(request):
    uname = request.POST["uname"]
    # uname = request.POST.get('uname')
    request.session["uname"] = uname
    return redirect("/booktest/session1/")


def session3(request):
    request.session["uname"] = None
    return redirect("/booktest/session1/")
