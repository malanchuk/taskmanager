# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, get_object_or_404, redirect
from tasks.models import Task, Comment, UserProfile
from django.template.context import RequestContext
from forms import CommentForm, TaskForm
from django.core.context_processors import csrf
from django.contrib import auth
from django.core.paginator import Paginator
from django.contrib.auth.models import User
# Create your views here.


#def detail(request, task_id):
"""task = get_object_or_404(Task, pk=task_id)
    comments = task.comment_set.all()
    print request.user.is_authenticated()
  # profile = request.user.get_profile()
  # profile = user.profile
    return render_to_response('tasks/detail.html', {'task': task, 'comments': comments},
        context_instance=RequestContext(request)) # 'profile': profile"""

# def user(request, user_id):
#	user = get_object_or_404(User, pk=user_id)
#	userprofile = get_object_or_404(UserProfile, user=user)
#	tasks = user.task_set.all()
#	return render_to_response('tasks/user.html', {'user': user, 'tasks': task})



def tasks(request, page_number=1):
    all_tasks = Task.objects.order_by('-start_date').all()
    current_page = Paginator(all_tasks, 10) 
    args = {}
    args.update(csrf(request))
    args['tasks'] = current_page.page(page_number)
    args['username'] = auth.get_user(request).username
    args['all_profiles'] = UserProfile.objects.all()
    return render_to_response('tasks.html', args)
    #return render_to_response('tasks.html', {'tasks': current_page.page(page_number), 'username':auth.get_user(request).username, })

def task(request, task_id=1):
    comment_form = CommentForm
    args = {}
    args.update(csrf(request))
    args['task'] = Task.objects.get(id=task_id)
    args['comments'] = Comment.objects.filter(task_id=task_id)
    args['form'] = comment_form
    args['username'] = auth.get_user(request).username
    args['all_profiles'] = UserProfile.objects.all()
    return render_to_response('task.html', args)


def addcomment(request, task_id):
    #if request.POST:
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.task = Task.objects.get(id=task_id)
        comment.user = request.user
        form.save()
    return redirect('/tasks/get/%s' % task_id)

def addtask(request, user_id): 
    user = get_object_or_404(User, pk=user_id) 
    task_form = TaskForm(request.POST)
    args = {}
    args.update(csrf(request))
    args['task_form'] = task_form
    args['username'] = auth.get_user(request).username
    args['all_profiles'] = UserProfile.objects.all()
    if task_form.is_valid():
        task = task_form.save(commit=False)
        task.author_id = request.user.id
        task_form.save()
    return render_to_response('addtask.html', args, context_instance=RequestContext(request))

