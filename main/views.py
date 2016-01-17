from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template('main/index.html')
    return HttpResponse(template.render(request))


def login(request):
    template = loader.get_template('main/Login.html')
    return HttpResponse(template.render(request))


def order(request):
    template = loader.get_template('main/Order.html')
    return HttpResponse(template.render(request))


def profile(request):
    template = loader.get_template('main/Profile.html')
    return HttpResponse(template.render(request))


def sign_up(request):
    template = loader.get_template('main/SingnUp.html')
    return HttpResponse(template.render(request))


def task_show(request):
    template = loader.get_template('main/Task.html')
    return HttpResponse(template.render(request))


def contact(request):
    template = loader.get_template('main/Contact.html')
    return HttpResponse(template.render(request))

