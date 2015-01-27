# -*- coding: utf8 -*-

from django.shortcuts import render
from django.http.response import HttpResponse, Http404    # импорт ответов браузера
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response, redirect
from task.models import Task, Comment, Profile            # импорт моделей для работы с базой данных
from django.core.exceptions import ObjectDoesNotExist
from forms import CommentForm, TaskForm                   # форма комментирования
from django.core.context_processors import csrf           # csrf - вид хакерской атаки
from django.core.paginator import Paginator               # модуль пагинации
from django.contrib import auth                           # auth - модуль для работы с пользователями
from django.contrib.auth.decorators import login_required # декоратор, позволяющий выполнять действия только залогиненым пользователям
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

def tasks(request, page_number=1):                        # дефолтное значение page_number=1
    all_tasks = Task.objects.all()   
                        # переменной all_articles передаём все статьи(но Джанго будет обрабатывать и вызывать их не все сразу, а только то количество, которое запрашивает Пагинатор, чтобы не нагружать базу)
    current_page = Paginator(all_tasks, 10)               # Модуль Paginator принимает all_articles. Создаём модель пагинации - базовая страница current_page будет содержать 2 статьи
  # order = Task.objects.order_by(‘-task_startdate’)[:5]
  # output = ', '.join([p.task_text for p in order])
    return render_to_response('tasks.html', 
        {'tasks': current_page.page(page_number), 
        'username': auth.get_user(request).username,
        'all_users': User.objects.all(),
        'all_profiles': Profile.objects.all(),
        })
# ((в шаблон передаётся articles.html, все статьи (Article.objects.all()), имя пользователя)) ЗАМЕНЕНО НА:
# 'articles': current_page.page(page_number) - передаём current_page, page(page_number) -номер страницы
# 'username': auth.get_user(request) - получить пользователя(get_user) и все его данные из request, и если он получен, то этот пользователь присваивается к переменной username
# 'username': auth.get_user(request).username - получить только содержимое ячейки username(имя пользователя) из request, и если оно получено, то это имя присваивается к переменной username


def task(request, task_id=1):
    comment_form = CommentForm
    args = {}                                             # создание нового пустого словаря
    args.update(csrf(request))                            # создаёт проверку вводимого текста в форму(защита) и добавляет ее в словарь
    args['task'] = Task.objects.get(id=task_id) 
    args['comments'] = Comment.objects.filter(comments_task_id=task_id)
    args['form'] = comment_form                           # создаём форму для передачи в шаблон
    args['username'] = auth.get_user(request).username    # получить имя пользователя username из request, и если оно получено, то это имя присваивается к переменной username
    args['all_profiles'] = Profile.objects.all()
    args['all_profiles'] = Profile.objects.all()
    return render_to_response('task.html', args)          # в шаблон передаётся article.html и все ед=лементы словаря(args)

# @login_required
def addcomment(request, task_id):                         # добавление комментов к статьям(не более 1 раза в 60 секунд)
    task = get_object_or_404(Task, pk=task_id)    
    form = CommentForm(request.POST)                      # переменная form будет экзампляром CommentForm, заносим в нее данные из запроса request.POST
    if form.is_valid():                                   # валидация формы - проверка на соответствие введёных данных тем, которые ожидает форма
        comment = form.save(commit=False)                 # получение комментария из формы, запрет на автоматическое сохранение формы в бд, comment становится "равным" комментарию
        comment.comments_task = task                      # поиск статьи, к которой пишем комментарий по rticle_id, присваиваем ее comment.comments_article(ассоциация статьи и коммента)
        comment.comments_user = request.user  
        form.save()
    return redirect('/tasks/get/%s' % task_id) 