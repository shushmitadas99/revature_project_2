Feature: login

  Scenario: Valid login Teacher #1
    Given I am at the teacher login page
    When I type in a tusername of "teacher1"
    And I type in a tpassword of "password1"
    And I click the tlogin button
    Then I should be redirected to the teacher homepage

  Scenario: Valid login Teacher #2
    Given I am at the teacher login page
    When I type in a tusername of "teacher2"
    And I type in a tpassword of "password2"
    And I click the tlogin button
    Then I should be redirected to the teacher homepage

  Scenario: Invalid login Teacher #1
    Given I am at the teacher login page
    When I type in a tusername of "asdasd"
    And I type in a tpassword of "password1"
    And I click the tlogin button
    Then I should stay on the teacher login page

  Scenario: Invalid login Teacher #2
    Given I am at the teacher login page
    When I type in a tusername of "teacher1"
    And I type in a tpassword of "asdasd"
    And I click the tlogin button
    Then I should stay on the teacher login page

  Scenario: Invalid login Teacher #3
    Given I am at the teacher login page
    When I type in a tusername of "asdasd"
    And I type in a tpassword of "asdasd"
    And I click the tlogin button
    Then I should stay on the teacher login page