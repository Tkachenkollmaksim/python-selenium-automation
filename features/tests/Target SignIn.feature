# Created by maksimtkachenko at 9/10/24
Feature: Test for Target Sign In
  # Enter feature description here
  Scenario: User can Sign In
    Given Open target.com
    When  Click Sign In
    Then   From right side navigation menu, click Sign In
    Then Verify Sign In form opened