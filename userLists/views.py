from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.


def home(request):
    if request.method == 'POST':
        form = ListForm(request.POST or None)

        if form.is_valid():
            form.save()
            all_items = List.objects.all
            messages.success(request,('Item add!'))
            return render(request, 'userLists/home.html', {'all_items': all_items})

    else:
        all_items = List.objects.all
        return render(request, 'userLists/home.html', {'all_items': all_items})


def delete(request, list_id):
    task = List.objects.get(pk=list_id)
    task.delete()
    messages.success(request, ('Item is kill...'))
    return redirect('List-home')


def about(request):
    return render(request, 'userLists/about.html')


def cross_off(request, list_id):
    task = List.objects.get(pk=list_id)
    task.completed = True
    task.save()
    return redirect('List-home')


def uncross(request, list_id):
    task = List.objects.get(pk=list_id)
    task.completed = False
    task.save()
    return redirect('List-home')


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