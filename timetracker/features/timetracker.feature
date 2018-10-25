Feature: completing a task

    Scenario: charge hours to a task
        Given i entered the form
        When i selected a project
        When i selected a developer
        When i selected a task from that developer and that project
        When i chose 6 hours
        When i chose a date
        When i submit the form
        Then task will have worked hours

    Scenario: charge 6 hour to a task
        Given i entered the form
        When i selected a project
        When i selected a developer
        When i selected a task from that developer and that project
        When i chose 6 hours
        When i chose a date
        When i submit the form
        Then task will have worked hours for that date

    Scenario: charge 6 hour to a task
        Given i entered the form
        When i selected a project
        When i selected a developer
        When i selected a task from that developer and that project
        When i chose 6 hours
        When i chose a date
        When i submit the form
        Then task will have worked hours for that date and hours

    Scenario: charge 6 hour to a task for different dates
        Given i entered the form
        When i selected a project
        When i selected a developer
        When i selected a task from that developer and that project
        When i chose 6 hours
        When i chose a date
        When i submit the form
        Then task will have worked hours for that date
        When i chose another date
        When i submit the form
        Then task will have two worked hours charged

    Scenario: charge 6 hour to a task for different dates
        Given i entered the form
        When i selected a project
        When i selected a developer
        When i selected a task from that developer and that project
        When i chose 6 hours
        When i chose a date
        When i submit the form
        Then task will have worked hours for that date and hours
        When i chose another date
        When i submit the form
        Then task will have worked hours for those dates and hours

    Scenario: can't charge hours to a task for the same date
        Given i entered the form
        When i selected a project
        When i selected a developer
        When i selected a task from that developer and that project
        When i chose 6 hours
        When i chose a date
        When i submit the form
        Then task will have worked hours for that date and hours
        When i submit the form
        Then task will have only one worked hours charged for that date

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