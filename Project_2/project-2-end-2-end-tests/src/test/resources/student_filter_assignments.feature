Feature: Filter assignments

  Scenario:
    Given I am at the student homepage #3
    When I click on View All Assignments #2
    And I click on the filter dropdown and select Science
    Then I can see only assignments for the Science course
