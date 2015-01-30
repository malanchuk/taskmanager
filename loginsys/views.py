# -*- coding: utf8 -*-
from django.shortcuts import render_to_response, redirect
from django.core.context_processors import csrf  # csrf - вид хакерской атаки
from django.contrib.auth.forms import UserCreationForm  # форма создания юзера при авторизации
from django.contrib import auth  # auth - модуль для работы с пользователями


def login(request):
    args = {}  # создаём словарь
    args.update(csrf(request))  # защита
    print "test"
    if request.POST:  # если данные авторизации получены
        username = request.POST.get('username',
                                    '')  # получить из ПОСТ-запроса 'username' и присвоить его пееременной username, если его там нет, то присвоиться '' (пустота, ничего). // Даные из формы авторизации попадают в ПОСТ-запрос под лекалом 'username', именно это значение будет присвоено переменной username
        password = request.POST.get('password',
                                    '')  # получить из ПОСТ-запроса 'password' и присвоить его пееременной password, если его там нет, то присвоиться '' (пустота, ничего)
        user = auth.authenticate(username=username,
                                 password=password)  # отправляем в модуль auth две переменных username и password
        if user is not None:  # если пользователь не None - тоесть существует и найден (если пользователь с такими значениями username и password не найден, то вернется значение None)
            auth.login(request, user)  # создаётся сессия для пользователя и он становиться авторизированным

            return redirect('/')  # редиррект на главную
        else:  # если пользователь не найден(not not None)
            args[
                'login_error'] = "Пользователь не найден"  # создаём переменную login_error со значением "Пользователь не найден"
            return render_to_response('login.html', args)  # возвращаем форму логина
    else:
        return render_to_response('login.html',
                                  args)  # если данные не переданы, отображаем форму регистрации login.html


def logout(request):
    auth.logout(request)  # деавторизация
    return redirect('/auth/login/')  # отправка на главную


def register(request):
    args = {}                                             
    args.update(csrf(request))      
    args['form'] = UserCreationForm()                     # создаём элемент словаря 'form' и присваеваем ему пустую форму
    if request.POST:                                      # проверка, получены ли данные
        newuser_form = UserCreationForm(request.POST)     # создаём новую форму, содержащую данные из запроса ПОСТ
        if newuser_form.is_valid():                       # проверка валидности(совпали ли пароли и тд)
            newuser_form.save()                           # сохранение в бд
            newuser = auth.authenticate(username=newuser_form.cleaned_data['username'], password=newuser_form.cleaned_data['password2']) # присваиваем в бд полям username и password в таблице нового пользователя значения, введённые пользователем в формы.
            auth.login(request, newuser)                  # тут же авторизируем пользователя в систему
            return redirect('/')                          # и перенаправляем на главную(вход в систему уже будет выполнен)
        else:                                             # если данные не валидные
            args['form'] = newuser_form                   # newuser_form добавляем в словарь 
    return render_to_response('register.html', args)      # render register.html