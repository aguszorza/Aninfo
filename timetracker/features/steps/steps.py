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


@when(u'i selected a task')
def step_impl(context):
    context.form['task'] = Task.objects.all()[0].id


@when(u'i chose 6 hours')
def step_impl(context):
    context.form['hours'] = 6

@when(u'i selected a task from other developer')
def step_impl(context):
    context.form['task'] = Task.objects.all()[10].id

@when(u'i submit the form')
def step_impl(context):
    url = "/timetracker/completeTask/"
    data = urlencode(context.form)
    context.response = context.test.client.post(url, data, content_type="application/x-www-form-urlencoded", follow=True)


@then(u'task will be completed')
def step_impl(context):
    assert Task.objects.get(pk=context.form['task']).completedTime > 0
    assert context.response.context['success']


@then(u'task will not be completed')
def step_impl(context):
    assert context.response.context['error']
    assert Task.objects.get(pk=context.form['task']).completedTime == 0
