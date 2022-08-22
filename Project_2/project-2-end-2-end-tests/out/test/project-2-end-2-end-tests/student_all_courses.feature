Feature: View all courses

  Scenario: View all courses
    Given I am at the student homepage #2
    When I click on View All Courses
    Then I should see all the courses for the student