from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.utils import timezone
from main.models import Member


def index(request):
    template = loader.get_template('main/index.html')
    return HttpResponse(template.render(request))


def login(request):
    context = dict()
    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        password = request.POST.get('password')
        try:
            obj = Member.objects.get(user_name=user_name, password=password)
        except:
            obj = None
        if obj is not None:
            pass
        else:
            context['not_match'] = True
    template = loader.get_template('main/Login.html')
    context['template'] = template
    return HttpResponse(template.render(context, request))


def order(request):
    template = loader.get_template('main/Order.html')
    return HttpResponse(template.render(request))


def profile(request):
    template = loader.get_template('main/Profile.html')
    return HttpResponse(template.render(request))


def sign_up(request):
    if request.method == 'POST':
        first_name = request.POST.get('fist_name')
        print(first_name)
        last_name = request.POST.get('last_name')
        print(last_name)
        email = request.POST.get('email')
        print(email)
        user_name = request.POST.get('user_name')
        print(user_name)
        password = request.POST.get('password')
        print(password)
        conf_password = request.POST.get('confirm_password')
        print(conf_password)
        if password != conf_password:
            result = 'password and confirm does not match!'
        else:
            member = Member(user_name=user_name, first_name=first_name, last_name=last_name, email=email, credit=0, debit=0, skill='developer', password=password, is_verified=True, join_date=timezone.now())
            member.save()
            result = 'account ' + user_name + ' successfully created.'
    else:
        result = None

    template = loader.get_template('main/SingnUp.html')
    context = dict()
    context['template'] = template
    context['result'] = result
    return HttpResponse(template.render(context, request))


def task_show(request):
    template = loader.get_template('main/Task.html')
    return HttpResponse(template.render(request))


def contact(request):
    template = loader.get_template('main/Contact.html')
    return HttpResponse(template.render(request))


def AddSkill(request):
    template = loader.get_template('main/AddSkill.html')
    return HttpResponse(template.render(request))


def EditProfile(request):
    template = loader.get_template('main/EditProfile.html')
    return HttpResponse(template.render(request))



