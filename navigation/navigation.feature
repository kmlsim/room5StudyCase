Feature: Navigate throug room5 website
  Scenario: User is able to enter on room5 website
    Given the room5 website
    When the user enter on it
    Then s/he is able to see the web page successfully

  Scenario: User is able to search for something
    Given the user is on the main page of room5
    When the s/he search for 'Brazil' on the search field
    Then the site will return his/her research.

  Scenario: User is able to change country preferences
    Given the user on the main page
    When s/he navigate to the botton of the page,
    And s/he changes the country option to 'Brazil'
    Then s/he will be redirect the contry choose page.

  Scenario: User is able to navigate throught the menu
    Given the menu on the room5 page
    When the user navigate through it
    Then s/he will be able to go to the pages it was selected.
  #
  # Scenario: User is able to see the content from the main page
  #   Given the user on the main page
  #   When s/he clicks on a content
  #   Then s/he will be addressed to the content page.
