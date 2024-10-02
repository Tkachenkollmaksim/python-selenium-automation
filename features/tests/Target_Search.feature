# Created by maksimtkachenko at 9/10/24
Feature: Test for Target Search Functionality
  # Enter feature description here

  Scenario: User can search for coffee
    Given Open the target.com
    When  Search for Coffee
    Then Verify that correct search results shown for Сoffee
    Then Verify product Coffee in URL


  Scenario: User can search for tea
    Given Open the target.com
    When  Search for Tea
    Then Verify that correct search results shown for tea


  Scenario Outline: User can search for product
    Given Open target.com
    When  Search for <search_word>
    Then Verify that correct search results shown for <search_results>
    Examples:
    |search_word | search_results |
    |coffee      | coffee         |
    |mug         | mug            |
    |tea         | tea            |