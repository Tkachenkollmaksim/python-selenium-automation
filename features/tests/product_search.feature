Feature: Test Scenarios for Search functionality

  Scenario: User can search for a product
    Given Open Google page
    When Input Car into search field
    And Click on search icon
    Then Product results for Car are shown

  Scenario: Verify user can search for a product
    Given Open the target.com
    When Search for Coffee Beans
    Then Verify that every product has a name and an image
