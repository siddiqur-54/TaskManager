from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from tasks.models import Task, TaskImage
from tasks.forms import TaskForm, TaskImageForm
from django.db.models import Case, When, Value
from django.db import models
# Create your views here.

@login_required
def task_list_search_view(request):
    query_dict = request.GET
    try:
        query = query_dict.get("query")
    except:
        query = None
    task_object_list = Task.objects.filter(user=request.user)
    task_object_search_list = None
    if query is not None:
       task_object_search_list = task_object_list.search(query=query)
    context = {
        'query' : query,
        'task_object_list' : task_object_list,
        'task_object_search_list' : task_object_search_list
    }
    return render(request, 'tasks/task_list_search.html', context)


@login_required
def task_create_view(request):
    task_form = TaskForm(request.POST or None)
    task_image_form = TaskImageForm(request.POST or None, request.FILES or None)
    context = {
        'task_form': task_form,
        'task_image_form': task_image_form,
    }
    if task_form.is_valid() and task_image_form.is_valid():
        task_object = task_form.save(commit=False)
        task_object.user = request.user
        task_object.save()
        images = request.FILES.getlist('image')
        for image in images:
            TaskImage.objects.create(task=task_object, image=image)
        context['created'] = True
        return redirect('/tasks/list-search-pending/')
    return render(request, 'tasks/task_create.html', context)


@login_required
def task_update_view(request, slug=None):
    task_object = get_object_or_404(Task, slug=slug, user=request.user)
    task_form = TaskForm(request.POST or None, instance=task_object)
    task_image_form = TaskImageForm(request.POST or None, request.FILES or None)
    task_image_list = TaskImage.objects.filter(task=task_object)
    context = {
        'task_form': task_form,
        'task_image_form': task_image_form,
        "task_image_list": task_image_list,
    }
    if task_form.is_valid() and task_image_form.is_valid():
        task_form.save()
        images = request.FILES.getlist('image')
        for image in images:
            TaskImage.objects.create(task=task_object, image=image)
        context['updated'] = True
        return redirect(task_object.get_absolute_url())
    return render(request, 'tasks/task_update.html', context)


@login_required
def task_delete_view(request, slug=None):
    task_object = Task.objects.get(user=request.user, slug=slug)
    if request.method == "POST":
        if task_object.pending == True:
            task_object.delete()
            return redirect('/tasks/list-search-pending/')
        else:
            task_object.delete()
            return redirect('/tasks/list-search-completed/')
    context = {
        'task_object' : task_object
    }
    return render(request, 'tasks/task_delete.html', context)


@login_required
def task_detail_view(request, slug=None):
    task_object = Task.objects.get(slug=slug)
    task_image_list = TaskImage.objects.filter(task=task_object)
    context = {
        "task_object": task_object,
        "task_image_list": task_image_list,
    }
    return render(request, 'tasks/task_detail.html', context)


@login_required
def mark_completed_view(request, slug=None):
    task_object = Task.objects.get(user=request.user, slug=slug)
    task_object.pending = False
    task_object.save()
    return redirect('/tasks/list-search-pending/')


@login_required
def mark_pending_view(request, slug=None):
    task_object = Task.objects.get(user=request.user, slug=slug)
    task_object.pending = True
    task_object.save()
    return redirect('/tasks/list-search-completed/')


@login_required
def task_image_delete_view(request, image_id):
    task_image = get_object_or_404(TaskImage, id=image_id)
    task_object = task_image.task
    if request.method == "POST":
        task_image.delete()
        return redirect(task_object.get_absolute_url())
    context = {
        'task_image' : task_image,
    }
    return render(request, 'tasks/task_image_delete.html', context)


@login_required
def task_list_view(request, filter=None):
    priority_filter = request.GET.get('priority', 'all')
    status_filter = request.GET.get('status', 'all')
    order_by_param = request.GET.get('order_by', '-created_at')
    task_list = Task.objects.filter(user=request.user)
    if priority_filter in ['L', 'M', 'H']:
        task_list = task_list.filter(priority=priority_filter)
    if status_filter in ['True', 'False']:
        task_list = task_list.filter(pending=(status_filter == 'True'))
    if order_by_param not in ['created_at', '-created_at', 'deadline', '-deadline']:
        order_by_param = '-created_at'
    task_list = task_list.order_by(order_by_param)
    context = {
        'task_list': task_list,
        'priority_filter': priority_filter,
        'status_filter': status_filter,
        'order_by_param': order_by_param,
    }
    return render(request, 'tasks/task_list_filter.html', context)