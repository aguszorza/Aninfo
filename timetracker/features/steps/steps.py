from behave import *
from django.http import HttpResponse, HttpResponseRedirect
from urllib.parse import urlencode
from psatimetracker.models import Task, Project, Developer
import datetime

@given('i entered the form')
def step_impl(context):
    context.form = {}

@when(u'i selected a project')
def step_impl(context):
    context.form['project'] = Project.objects.all()[0].id


@when(u'i selected a developer')
def step_impl(context):
    context.form['developer'] = Developer.objects.all()[0].id

@when(u'i select another developer')
def step_impl(context):
    context.form['oldDeveloper'] = context.form['developer']
    context.form['developer'] = Developer.objects.exclude(id=context.form['oldDeveloper'])[0].id
    assert context.form['developer'] != context.form['oldDeveloper']


@when(u'i selected a task from that developer and that project')
def step_impl(context):
    context.form['task'] = Task.objects.filter(project__id = context.form['project'], 
                                                developers__id = context.form['developer'])[0].id


@when(u'i chose 6 hours')
def step_impl(context):
    context.form['hours'] = 6

@when(u'i chose 8 hours')
def step_impl(context):
    context.form['oldHours'] = context.form['hours']
    context.form['hours'] = 8

@when(u'i chose a lot of hours')
def step_impl(context):
    context.form['hours'] = 32

@when(u'i chose negative hours')
def step_impl(context):
    context.form['hours'] = -1

@when(u'i chose 0 hours')
def step_impl(context):
    context.form['hours'] = 0

@when(u'i chose a date')
def step_impl(context):
    context.form['date'] = '2018-10-17'

@when(u'i chose another date')
def step_impl(context):
    context.form['oldDate'] = context.form['date']
    context.form['date'] = '2018-10-18'
    assert context.form['date'] != context.form['oldDate']

@when(u'i chose a future date')
def step_impl(context):
    context.form['date'] = datetime.date.today() + datetime.timedelta(days = 2) 

@when(u'i chose today')
def step_impl(context):
    context.form['date'] = datetime.date.today()



@when(u'i selected a task from other developer')
def step_impl(context):
    context.form['task'] = Task.objects.filter(project__id = context.form['project']).exclude(
                                                developers__id = context.form['developer'])[0].id

@when(u'i selected a task from other project')
def step_impl(context):
    context.form['task'] = Task.objects.exclude(project__id = context.form['project']).filter(
                                                developers__id = context.form['developer'])[0].id

@when(u'i selected a task for all developers')
def step_impl(context):
    tasks = Task.objects.filter(project__id = context.form['project'])
    for task in tasks:
        if task.developers.count() > 2:
            context.form['task'] = task.id
            break


@when(u'i submit the form')
def step_impl(context):
    url = "/timetracker/completeTaskHours/"
    data = urlencode(context.form)
    context.response = context.test.client.post(url, data, content_type="application/x-www-form-urlencoded", follow=True)


@then(u'task will have worked hours')
def step_impl(context):
    assert len(Task.objects.get(pk=context.form['task']).workedhours_set.all()) > 0
    assert context.response.context['success']

@then(u'task will have two worked hours charged')
def step_impl(context):
    assert len(Task.objects.get(pk=context.form['task']).workedhours_set.all()) == 2
    assert context.response.context['success']


@then(u'task will have worked hours for that date and developer')
def step_impl(context):
    assert len(Task.objects.get(pk=context.form['task']).workedhours_set.filter(date = context.form['date'], developer=context.form['developer'])) > 0
    assert context.response.context['success']

@then(u'task will have worked hours for that date and hours and developer')
def step_impl(context):
    assert len(Task.objects.get(pk=context.form['task']).workedhours_set.filter(date = context.form['date'], hours = context.form['hours'], developer=context.form['developer'])) > 0
    assert context.response.context['success']

@then(u'task will have worked hours for those dates and hours and developer')
def step_impl(context):
    assert len(Task.objects.get(pk=context.form['task']).workedhours_set.filter(date = context.form['date'], hours = context.form['hours'], developer=context.form['developer'])) > 0
    assert len(Task.objects.get(pk=context.form['task']).workedhours_set.filter(date = context.form['oldDate'], hours = context.form['hours'], developer=context.form['developer'])) > 0
    assert context.response.context['success']

@then(u'task will not have worked hours')
def step_impl(context):
    assert len(Task.objects.get(pk=context.form['task']).workedhours_set.all()) == 0
    assert context.response.context['error']

@then(u'task will have only one worked hours charged for that date and developer')
def step_impl(context):
    assert len(Task.objects.get(pk=context.form['task']).workedhours_set.filter(date = context.form['date'], developer=context.form['developer'])) == 1
    assert context.response.context['error']

@then(u'task will have worked hours for those developers')
def step_impl(context):
    assert context.response.context['success']
    assert len(Task.objects.get(pk=context.form['task']).workedhours_set.filter(developer=context.form['developer'])) == 1
    assert len(Task.objects.get(pk=context.form['task']).workedhours_set.filter(developer=context.form['oldDeveloper'])) == 1

@then(u'task will have worked hours for those developers with those hours and date')
def step_impl(context):
    assert context.response.context['success']
    assert len(Task.objects.get(pk=context.form['task']).workedhours_set.filter(date = context.form['date'], hours = context.form['hours'],developer=context.form['developer'])) == 1
    assert len(Task.objects.get(pk=context.form['task']).workedhours_set.filter(date = context.form['date'], hours = context.form['oldHours'],developer=context.form['oldDeveloper'])) == 1

@then(u'task will have worked hours for those developers with those hours and dates')
def step_impl(context):
    assert context.response.context['success']
    assert len(Task.objects.get(pk=context.form['task']).workedhours_set.filter(date = context.form['date'], hours = context.form['hours'],developer=context.form['developer'])) == 1
    assert len(Task.objects.get(pk=context.form['task']).workedhours_set.filter(date = context.form['oldDate'], hours = context.form['oldHours'],developer=context.form['oldDeveloper'])) == 1

