Feature: View all assignments

  Scenario: View all assignments
    Given I am at the student homepage
    When I click on View All Assignments
    Then I should see all the submitted assignments for the student