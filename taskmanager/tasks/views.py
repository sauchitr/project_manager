from django.shortcuts import render, get_object_or_404, redirect
from .models import Project, Task
from .forms import ProjectForm, TaskForm, UserRegisterForm
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required
def project_list(request):
    projects = Project.objects.all()
    return render(request, 'tasks/project_list.html', {'projects': projects})


@login_required
def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    tasks = Task.objects.filter(project=project)
    return render(request, 'tasks/project_detail.html', {'project': project, 'tasks': tasks})


@login_required
def project_create(request):
    form = ProjectForm(request.POST or None)
    if form.is_valid():
        project = form.save(commit=False)
        project.save()
        return redirect('project_list')
    return render(request, 'tasks/project_form.html', {'form': form})


@login_required
def project_update(request, pk):
    project = get_object_or_404(Project, pk=pk)
    form = ProjectForm(request.POST or None, instance=project)
    if form.is_valid():
        project = form.save(commit=False)
        project.save()
        return redirect('project_detail', pk=project.pk)
    return render(request, 'tasks/project_form.html', {'form': form})


@login_required
def project_delete(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        project.delete()
        messages.success(request, f'The project "{project.name}" has been deleted.')
        return redirect('project_list')
    return render(request, 'tasks/project_confirm_delete.html', {'project': project})


@login_required
def task_create(request, pk):
    project = get_object_or_404(Project, pk=pk)
    form = TaskForm(request.POST or None)
    if form.is_valid():
        task = form.save(commit=False)
        task.project = project
        task.save()
        return HttpResponseRedirect(reverse('project_detail', args=(pk,)))
    return render(request, 'tasks/task_form.html', {'form': form, 'project': project})


@login_required
def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    project = task.project
    form = TaskForm(request.POST or None, instance=task)
    if request.method == 'POST':
        if 'delete' in request.POST:
            task.delete()
            return redirect('project_detail', pk=project.pk)
        elif form.is_valid():
            task = form.save(commit=False)
            task.project = project
            task.save()
            messages.success(request, f'The task "{task.name}" has been updated.')
            return redirect('project_detail', pk=project.pk)
    return render(request, 'tasks/task_form.html', {'form': form, 'project': project})


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Your account is created. Kindly login")
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, "tasks/register.html", {"form": form})
