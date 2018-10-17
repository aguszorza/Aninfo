Feature: completing a task

    Scenario: complete a task
        Given i entered the form
        When i selected a project
        When i selected a developer
        When i selected a task from that developer and that project
        When i chose 6 hours
        When i chose a date
        When i submit the form
        Then task will have worked hours

    Scenario: complete a 6 hour task
        Given i entered the form
        When i selected a project
        When i selected a developer
        When i selected a task from that developer and that project
        When i chose 6 hours
        When i chose a date
        When i submit the form
        Then task will have worked hours for that date

    Scenario: complete a 6 hour task
        Given i entered the form
        When i selected a project
        When i selected a developer
        When i selected a task from that developer and that project
        When i chose 6 hours
        When i chose a date
        When i submit the form
        Then task will have worked hours for that date and hours

    Scenario: don't charge hours to another developer's task 
        Given i entered the form
        When i selected a project
        When i selected a developer
        When i selected a task from other developer
        When i chose 6 hours
        When i chose a date
        When i submit the form
        Then task will not have worked hours

    Scenario: don't charge hours to another project's task 
        Given i entered the form
        When i selected a project
        When i selected a developer
        When i selected a task from other project
        When i chose 6 hours
        When i chose a date
        When i submit the form
        Then task will not have worked hours