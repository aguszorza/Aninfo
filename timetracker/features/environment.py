from psatimetracker.models import Task, Project, Developer

def before_scenario(context, scenario):
    names = ['Pepe Perez', 'Jose Juarez', 'Fernando Fernandez', 'Rodrigo Rodriguez']
    for person in names:
        dev = Developer(name = person)
        dev.save()

    names = ['Proyecto 1', 'Proyecto 2']
    for project in names:
        p = Project(name = project)
        p.save()

    for project in Project.objects.all():
        task = Task(name = "Tarea para todos", project=project)
        task.save()
        for dev in Developer.objects.all():
            task.developers.add(dev)
            for i in range (1,4):
                dev.task_set.create(name = "Tarea " + str(i) + ": " + dev.name, project=project)
