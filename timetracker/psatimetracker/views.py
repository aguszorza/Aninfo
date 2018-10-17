from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import Developer, Task, Project


def index(request, success='', error=''):
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


def completeTaskHours(request):
    try:
        project = get_object_or_404(Project, pk=request.POST['project'])
        developer = get_object_or_404(Developer, pk=request.POST['developer'])
        task = get_object_or_404(Task, pk=request.POST['task'])
        hours = request.POST['hours']
        date = request.POST['date']

        error = validateData(project, developer, task, hours, date)
        if (error):
            return index(request, error=error)

        saveHours(task, hours, date)
        return HttpResponseRedirect(reverse('psatimetracker:completedTaskHours'))

    except:
        return index(request, error='Ocurrio un error')


def validateData(project, developer, task, hours, date):
    if (task.developer != developer):
            return 'La tarea seleccionada no pertenece al desarrollador'

    if (task.project != project):
        return 'La tarea seleccionada no pertenece al proyecto'

    return ''

def saveHours(task, hours, date):
    task.workedhours_set.create(hours = hours, date = date)

def taskHoursCompleted(request):
    return index(request, success='True')