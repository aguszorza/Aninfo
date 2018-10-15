from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import Developer, Task, Project


def index(request, success=False, error=''):
    developers = Developer.objects.all()
    projects = Project.objects.all()
    tasks = Task.objects.all()

    context = {
        'developers': developers,
        'projects': projects,
        'tasks': tasks,
        'success': success,
        'error': error
    }
    return render(request, 'form.html', context)


def completeTask(request):
    try:
        project = get_object_or_404(Project, pk=request.POST['project'])
        developer = get_object_or_404(Developer, pk=request.POST['developer'])
        task = get_object_or_404(Task, pk=request.POST['task'])
        hours = request.POST['hours']
    except (KeyError):
        return index(request, error='Ocurrio un error')
    else:

        if (task.developer != developer):
            return index(request, error='La tarea seleccionada no pertenece al desarrollador')

        if (task.project != project):
            return index(request, error='La tarea seleccionada no pertenece al proyecto')

        task.completedTime = hours
        task.save()
        
        return HttpResponseRedirect(reverse('psatimetracker:taskCompleted'))


def taskCompleted(request):
    return index(request, success=True)