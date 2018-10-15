Feature: completing a task

    Scenario: complete a task
        Given i entered the form
        When i selected a project
        When i selected a developer
        When i selected a task from that developer and that project
        When i chose 6 hours
        When i submit the form
        Then task will be completed

    Scenario: complete a 6 hour task
        Given i entered the form
        When i selected a project
        When i selected a developer
        When i selected a task from that developer and that project
        When i chose 6 hours
        When i submit the form
        Then task will be completed with 6 hours

    Scenario: don't complete a task of other developer
        Given i entered the form
        When i selected a project
        When i selected a developer
        When i selected a task from other developer
        When i chose 6 hours
        When i submit the form
        Then task will not be completed