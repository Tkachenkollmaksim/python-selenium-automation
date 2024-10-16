# Created by maksimtkachenko at 10/11/24
Feature: # Enter feature name here
  # Enter feature description here

  Scenario: User can open and close Terms and Conditions from sign in page
    Given Open sign in page
    When Click Sign In
    And Click Nav Sign In
    When Store original window
    And Click on Target terms and conditions link
    And Switch to the newly opened window
    Then Verify Terms and Conditions page is opened
    And Close new window
    And Switch back to original