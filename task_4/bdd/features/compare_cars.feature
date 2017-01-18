Feature: Compare cars

  Scenario: Compare two cars
    Given I have no cars to compare
    When I select two random cars with parameters present
    And I click Compare Side by Side button on second car
    And Compare page opens
    And I enter first car data and click Compare button
    Then Cars parameters should be verified


