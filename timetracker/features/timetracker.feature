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
        Then task will have worked hours for that date and developer

    Scenario: charge 6 hour to a task
        Given i entered the form
        When i selected a project
        When i selected a developer
        When i selected a task from that developer and that project
        When i chose 6 hours
        When i chose a date
        When i submit the form
        Then task will have worked hours for that date and hours and developer

    Scenario: charge 6 hour to a task for different dates
        Given i entered the form
        When i selected a project
        When i selected a developer
        When i selected a task from that developer and that project
        When i chose 6 hours
        When i chose a date
        When i submit the form
        Then task will have worked hours for that date and developer
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
        Then task will have worked hours for that date and hours and developer
        When i chose another date
        When i submit the form
        Then task will have worked hours for those dates and hours and developer

    Scenario: charge 6 hour to a task for different developers in the same date
        Given i entered the form
        When i selected a project
        When i selected a developer
        When i selected a task for all developers
        When i chose 6 hours
        When i chose a date
        When i submit the form
        Then task will have worked hours for that date and hours and developer
        When i select another developer
        When i submit the form
        Then task will have worked hours for those developers

    Scenario: charge different hour to a task for different developers in the same date
        Given i entered the form
        When i selected a project
        When i selected a developer
        When i selected a task for all developers
        When i chose 6 hours
        When i chose a date
        When i submit the form
        Then task will have worked hours for that date and hours and developer
        When i select another developer
        When i chose 8 hours
        When i submit the form
        Then task will have worked hours for those developers

    Scenario: charge different hour to a task for different developers in the same date
        Given i entered the form
        When i selected a project
        When i selected a developer
        When i selected a task for all developers
        When i chose 6 hours
        When i chose a date
        When i submit the form
        Then task will have worked hours for that date and hours and developer
        When i select another developer
        When i chose 8 hours
        When i submit the form
        Then task will have worked hours for those developers with those hours and date

    Scenario: charge different hour to a task for different developers in different dates
        Given i entered the form
        When i selected a project
        When i selected a developer
        When i selected a task for all developers
        When i chose 6 hours
        When i chose a date
        When i submit the form
        Then task will have worked hours for that date and hours and developer
        When i select another developer
        When i chose another date
        When i chose 8 hours
        When i submit the form
        Then task will have worked hours for those developers with those hours and dates

    Scenario: can't charge hours to a task for the same date
        Given i entered the form
        When i selected a project
        When i selected a developer
        When i selected a task from that developer and that project
        When i chose 6 hours
        When i chose a date
        When i submit the form
        Then task will have worked hours for that date and hours and developer
        When i submit the form
        Then task will have only one worked hours charged for that date and developer

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

    Scenario: can't charge a lot of hours to a task 
        Given i entered the form
        When i selected a project
        When i selected a developer
        When i selected a task from that developer and that project
        When i chose a lot of hours
        When i chose a date
        When i submit the form
        Then task will not have worked hours

    Scenario: can't charge negative hours to a task 
        Given i entered the form
        When i selected a project
        When i selected a developer
        When i selected a task from that developer and that project
        When i chose negative hours
        When i chose a date
        When i submit the form
        Then task will not have worked hours

    Scenario: can't charge 0 hours to a task 
        Given i entered the form
        When i selected a project
        When i selected a developer
        When i selected a task from that developer and that project
        When i chose 0 hours
        When i chose a date
        When i submit the form
        Then task will not have worked hours

    Scenario: can't charge hours to a future date 
        Given i entered the form
        When i selected a project
        When i selected a developer
        When i selected a task from that developer and that project
        When i chose 6 hours
        When i chose a future date
        When i submit the form
        Then task will not have worked hours

    Scenario: can charge hours today
        Given i entered the form
        When i selected a project
        When i selected a developer
        When i selected a task from that developer and that project
        When i chose 6 hours
        When i chose today
        When i submit the form
        Then task will have worked hours