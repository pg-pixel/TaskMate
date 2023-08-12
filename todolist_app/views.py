from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from todolist_app.models import TodoList
from todolist_app.forms import TodoListForm

# Create your views here.
@login_required
def todolist(request):
    if request.method == 'POST':
        form = TodoListForm(request.POST or None)
        if form.is_valid():
            form.save(commit=False).Manager = request.user
            form.save()
            messages.success(request, 'Task has been added!')
        return redirect('todolist')
    else:
        all_tasks = TodoList.objects.filter(Manager = request.user)
        paginator = Paginator(all_tasks, 5)
        page = request.GET.get('pg')
        all_tasks = paginator.get_page(page)
        context = {
            'all_tasks':all_tasks,
        }
        return render(request, 'todolist.html', context)

@login_required   
def delete_task(request, task_id):
    task = TodoList.objects.get(pk = task_id)
    if task.Manager == request.user:
        task.delete()
    else:
        messages.error(request, 'Access restricted!')
    
    return redirect('todolist')

@login_required
def edit_task(request, task_id):
    if request.method == 'POST':
        curr_task = TodoList.objects.get(pk = task_id)
        form = TodoListForm(request.POST or None, instance = curr_task)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task has been Updated!')
            
        if request.POST.get('redirect'):            
            return HttpResponseRedirect(request.POST.get('redirect'))
    else:
        curr_tasks = TodoList.objects.get(pk = task_id)
        previous_page = request.META.get('HTTP_REFERER') 
        
        context = {
            'task':curr_tasks,
            'previous_page': previous_page,
        }
        return render(request, 'edit.html', context)

@login_required   
def mark_completed(request, task_id):
    curr_task = TodoList.objects.get(pk= task_id)
    if curr_task.Manager == request.user:
        curr_task.Done = True 
        curr_task.save()
    else:
        messages.error(request, 'Access restricted!')
    
    return redirect(request.META['HTTP_REFERER'])
 
@login_required   
def mark_pending(request, task_id):
    curr_task = TodoList.objects.get(pk= task_id)
    if curr_task.Manager == request.user:
        curr_task.Done = False 
        curr_task.save()
    else:
        messages.error(request, 'Access restricted!')
    
    return redirect(request.META['HTTP_REFERER'])
    
def contact_us(request):
    context = {
        'welcome_text':'Welcome to Conatct us page!'
    }
    return render(request, 'contact.html', context)

def about_us(request):
    context = {
        'welcome_text':'Welcome to about us!'
    }
    return render(request, 'about.html', context)

def index(request):
    context = {
        'welcome_text':'Welcome to Home!'
    }
    return render(request, 'index.html', context)