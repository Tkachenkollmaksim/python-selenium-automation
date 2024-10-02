# Created by maksimtkachenko at 9/10/24
Feature: Test for Target Search Functionality
  # Enter feature description here

  Scenario: User can see Cart Empty Message
    Given Open target.com
    When  Click on Cart icon
    Then Verify Cart Empty results shown


