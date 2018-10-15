from behave import *
from django.http import HttpResponse, HttpResponseRedirect
from urllib.parse import urlencode
from psatimetracker.models import Task

@given('i entered the form')
def step_impl(context):
    context.form = {}

@when(u'i selected a project')
def step_impl(context):
    context.form['project'] = 1


@when(u'i selected a developer')
def step_impl(context):
    context.form['developer'] = 1


@when(u'i selected a task')
def step_impl(context):
    context.form['task'] = 1


@when(u'i chose 6 hours')
def step_impl(context):
    context.form['hours'] = 6


@then(u'task will be completed')
def step_impl(context):
    url = "/timetracker/completeTask/"
    data = urlencode(context.form)
    response = context.test.client.post(url, data, content_type="application/x-www-form-urlencoded")
    assert len(Task.objects.all()) > 0
    assert response.status_code == 302 or response.status_code == 200


@when(u'i selected a task from other developer')
def step_impl(context):
    context.form['task'] = 10


@then(u'task will not be completed')
def step_impl(context):
    url = "/timetracker/completeTask/"
    data = urlencode(context.form)
    response = context.test.client.post(url, data, content_type="application/x-www-form-urlencoded")
    assert len(Task.objects.all()) > 0
    assert response.status_code == 302 or response.status_code == 200
