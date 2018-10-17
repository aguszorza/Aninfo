from behave import *
from django.http import HttpResponse, HttpResponseRedirect
from urllib.parse import urlencode
from psatimetracker.models import Task, Project, Developer

@given('i entered the form')
def step_impl(context):
    context.form = {}

@when(u'i selected a project')
def step_impl(context):
    context.form['project'] = Project.objects.all()[0].id


@when(u'i selected a developer')
def step_impl(context):
    context.form['developer'] = Developer.objects.all()[0].id


@when(u'i selected a task from that developer and that project')
def step_impl(context):
    context.form['task'] = Task.objects.filter(project__id = context.form['project'], 
                                                developer__id = context.form['developer'])[0].id


@when(u'i chose 6 hours')
def step_impl(context):
    context.form['hours'] = 6

@when(u'i chose a date')
def step_impl(context):
    context.form['date'] = '2018-10-17'


@when(u'i selected a task from other developer')
def step_impl(context):
    context.form['task'] = Task.objects.filter(project__id = context.form['project']).exclude(
                                                developer__id = context.form['developer'])[0].id

@when(u'i selected a task from other project')
def step_impl(context):
    context.form['task'] = Task.objects.exclude(project__id = context.form['project']).filter(
                                                developer__id = context.form['developer'])[0].id

@when(u'i submit the form')
def step_impl(context):
    url = "/timetracker/completeTaskHours/"
    data = urlencode(context.form)
    context.response = context.test.client.post(url, data, content_type="application/x-www-form-urlencoded", follow=True)


@then(u'task will have worked hours')
def step_impl(context):
    assert len(Task.objects.get(pk=context.form['task']).workedhours_set.all()) > 0
    assert context.response.context['success']

@then(u'task will have worked hours for that date')
def step_impl(context):
    assert len(Task.objects.get(pk=context.form['task']).workedhours_set.filter(date = context.form['date'])) > 0
    assert context.response.context['success']

@then(u'task will have worked hours for that date and hours')
def step_impl(context):
    assert len(Task.objects.get(pk=context.form['task']).workedhours_set.filter(date = context.form['date'], hours = context.form['hours'])) > 0
    assert context.response.context['success']

@then(u'task will not have worked hours')
def step_impl(context):
    assert len(Task.objects.get(pk=context.form['task']).workedhours_set.all()) == 0
    assert context.response.context['error']
