from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .forms import SignUp, Login
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from IPython import embed

def index(request):
    template = loader.get_template('homepage/show.html')
    context = {'SignUp': SignUp(),
               'Login': Login()}
    return HttpResponse(template.render(context, request))

def sign_up(request):
    if request.method == 'POST':
        form = SignUp(request.POST)
        if form.is_valid():
            user_data = form.cleaned_data
            if User.objects.filter(username=user_data['username']).exists():
                template = loader.get_template('homepage/show.html')
                context = {'SignUp': SignUp(),
                           'Login': Login()}
                return HttpResponse(template.render(context, request))
            else:
                user = User.objects.create_user(user_data['username'],
                                         user_data['email'],
                                         user_data['password'])
                login(request, user)
                return redirect('/user_page')

def login_user(request):
    u_name = request.POST['username']
    p_word = request.POST['password']

    user = authenticate(request, username=u_name, password=p_word)
    if user is not None:
        login(request, user)
        return redirect('/user_page')
    else:
        template = loader.get_template('homepage/show.html')
        context = {'SignUp': SignUp(),
                   'Login': Login()}
        return HttpResponse(template.render(context, request))

def user_page(request):
    template = loader.get_template('user/show.html')
    name = request.user.username
    context = {'name': name}
    return HttpResponse(template.render(context, request))

def logout_user(request):
    logout(request)
    template = loader.get_template('homepage/show.html')
    context = {'SignUp': SignUp(),
               'Login': Login()}
    return HttpResponse(template.render(context, request))
