Feature: completing a task

    Scenario: complete a task
        Given i entered the form
        When i selected a project
        When i selected a developer
        When i selected a task
        When i chose 6 hours
        Then task will be completed

    Scenario: complete a task of other developer
        Given i entered the form
        When i selected a project
        When i selected a developer
        When i selected a task from other developer
        When i chose 6 hours
        Then task will not be completed