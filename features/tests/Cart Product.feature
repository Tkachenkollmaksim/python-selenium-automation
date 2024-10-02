# Created by maksimtkachenko at 9/17/24
Feature: # Enter feature name here
  # Enter feature description here

  Scenario: User can see product in cart
    Given Open the target.com
    When  Search for Coffee
    When Click on Add to Cart button
    Then Store product name
    Then Verify adding to cart from side navigation
    Then Open cart page
    Then Verify cart has 1 item(s)
    And Verify cart has correct product