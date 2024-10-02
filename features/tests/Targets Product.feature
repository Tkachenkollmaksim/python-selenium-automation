# Created by maksimtkachenko at 9/16/24
Feature: # Enter feature name here
  # Enter feature description here

  Scenario: User can put products in cart
    Given Open the target.com
    When Search for Table
    Then Click on Add to Cart button
    And Store product name
    And Confirm Add to Cart button from side navigation
    And Open cart page
    Then Verify cart has 1 item(s)
    And Verify cart has correct product