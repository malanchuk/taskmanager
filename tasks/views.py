# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, get_object_or_404, redirect
from tasks.models import Task, Comment, UserProfile
from django.template.context import RequestContext
from forms import CommentForm
from django.core.context_processors import csrf
from django.contrib import auth
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



def tasks(request):                     
    return render_to_response('tasks.html', {'tasks': Task.objects.all(), 'username':auth.get_user(request).username})

def task(request, task_id=1):
    comment_form = CommentForm
    args = {}
    args.update(csrf(request))
    args['task'] = Task.objects.get(id=task_id)
    args['comments'] = Comment.objects.filter(task_id=task_id)
    args['form'] = comment_form
    args['username'] = auth.get_user(request).username
    return render_to_response('task.html', args)


def addcomment(request, task_id):
    #if request.POST:
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.task = Task.objects.get(id=task_id)
        form.save()
    return redirect('/tasks/get/%s' % task_id)


