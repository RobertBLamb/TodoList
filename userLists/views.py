from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm
from django.contrib import messages
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required()
def home(request):
    if request.method == 'POST':
        form = ListForm(request.POST or None)
        form.instance.author = request.user
        if form.is_valid():
            form.save()
            all_items = List.objects.filter(author=User.objects.get(username=request.user))
            messages.success(request,('Item add!'))
            return render(request, 'userLists/home.html', {'all_items': all_items})

    else:
        all_items = List.objects.filter(author=User.objects.get(username=request.user))
        return render(request, 'userLists/home.html', {'all_items': all_items})


def delete(request, list_id):
    task = List.objects.get(pk=list_id)
    task.delete()
    messages.success(request, ('Item is kill...'))
    return redirect('List-home')


def about(request):
    return render(request, 'userLists/about.html')


def cross_off(request, list_id, freq):
    task = List.objects.get(pk=list_id)
    task.completed = True
    task.save()
    return redirect(freq)


def uncross(request, list_id, freq):
    task = List.objects.get(pk=list_id)
    task.completed = False
    task.save()
    return redirect(freq)


def edit(request, list_id):
    if request.method == 'POST':
        task = List.objects.get(pk=list_id)

        form = ListForm(request.POST or None, instance=task)

        if form.is_valid():
            form.save()
            messages.success(request,('Item Change!'))
            return redirect('List-home')

    else:
        task = List.objects.get(pk=list_id)
        return render(request, 'userLists/edit.html', {'task': task})

@login_required()
def once(request):
    if request.method == 'POST':
        form = ListForm(request.POST or None)
        form.instance.author = request.user

        if form.is_valid():
            form.save()
            all_items = List.objects.filter(author=User.objects.get(username=request.user))
            messages.success(request,('Item add!'))
            return render(request, 'userLists/once.html', {'all_items': all_items})

    else:
        all_items = List.objects.filter(author=User.objects.get(username=request.user))
        return render(request, 'userLists/once.html', {'all_items': all_items})

@login_required()
def daily(request):
    if request.method == 'POST':
        form = ListForm(request.POST or None)
        form.instance.author = request.user

        if form.is_valid():
            form.save()
            all_items = List.objects.filter(author=User.objects.get(username=request.user))
            messages.success(request,('Item add!'))
            return render(request, 'userLists/daily.html', {'all_items': all_items})

    else:
        all_items = List.objects.filter(author=User.objects.get(username=request.user))
        return render(request, 'userLists/daily.html', {'all_items': all_items})

@login_required()
def weekly(request):
    if request.method == 'POST':
        form = ListForm(request.POST or None)
        form.instance.author = request.user

        if form.is_valid():
            form.save()
            all_items = List.objects.filter(author=User.objects.get(username=request.user))
            messages.success(request,('Item add!'))
            return render(request, 'userLists/weekly.html', {'all_items': all_items})

    else:
        all_items = List.objects.filter(author=User.objects.get(username=request.user))
        return render(request, 'userLists/weekly.html', {'all_items': all_items})

@login_required()
def monthly(request):
    if request.method == 'POST':
        form = ListForm(request.POST or None)
        form.instance.author = request.user

        if form.is_valid():
            form.save()
            all_items = List.objects.filter(author=User.objects.get(username=request.user))
            messages.success(request,('Item add!'))
            return render(request, 'userLists/monthly.html', {'all_items': all_items})

    else:
        all_items = List.objects.filter(author=User.objects.get(username=request.user))
        return render(request, 'userLists/monthly.html', {'all_items': all_items})