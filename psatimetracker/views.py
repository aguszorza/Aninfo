from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import Developer, Task, Project
from datetime import datetime


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

        developer.assignWorkedHours(task, hours, date)
        return HttpResponseRedirect(reverse('psatimetracker:completedTaskHours'))

    except:
        return index(request, error='Ocurrio un error')


def validateData(project, developer, task, hours, date):
    if len(task.developers.filter(id = developer.id)) == 0:
            return 'La tarea seleccionada no pertenece al desarrollador'

    if (task.project != project):
        return 'La tarea seleccionada no pertenece al proyecto'

    if (len(task.workedhours_set.filter(date = date, developer=developer)) > 0):
        return 'La tarea seleccionada ya tiene horas cargadas en esa fecha para ese desarrollador'

    if (int(hours) <= 0 or int(hours) >24):
        return 'La cantidad de horas es invalida'

    now = datetime.now().strftime('%Y-%m-%d')

    if (date > now):
        return 'La fecha es futura'

    return ''


def taskHoursCompleted(request):
    return index(request, success='True')