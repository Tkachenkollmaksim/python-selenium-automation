# Created by maksimtkachenko at 9/10/24
  @smoke
Feature: Test for Target Sign In
  # Enter feature description here
#  Scenario: User can Sign In
#    Given Open target.com
#    When  Click Sign In
#    Then   From right side navigation menu, click Sign In
#    Then Verify Sign In form opened
#
  Scenario: Can't find account
    Given Open target.com
    When  Click Sign In
    Then   From right side navigation menu, click Sign In
    Then Verify Sign In form opened
    When Enter username@gmail.com for email
    When Enter badPas$word123 for password
    Then Click Sign In button
    And Verify account is not found