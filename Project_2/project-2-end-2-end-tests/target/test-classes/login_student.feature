Feature: login

  Scenario: Valid login Student #1
    Given I am at the student login page
    When I type in a susername of "student1"
    And I type in a spassword of "password1"
    And I click the slogin button
    Then I should be redirected to the student homepage

  Scenario: Valid login Student #2
    Given I am at the student login page
    When I type in a susername of "student2"
    And I type in a spassword of "password2"
    And I click the slogin button
    Then I should be redirected to the student homepage

  Scenario: Invalid login Student #1
    Given I am at the student login page
    When I type in a susername of "asdasd"
    And I type in a spassword of "password1"
    And I click the slogin button
    Then I should stay on the student login page

  Scenario: Invalid login Student #2
    Given I am at the student login page
    When I type in a susername of "student1"
    And I type in a spassword of "asdasd"
    And I click the slogin button
    Then I should stay on the student login page

  Scenario: Invalid login Student #3
    Given I am at the student login page
    When I type in a susername of "asdasd"
    And I type in a spassword of "asdasd"
    And I click the slogin button
    Then I should stay on the student login page


