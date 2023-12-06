Feature: Registration on demoqa.com

  Scenario: Registration on demoqa.com with valid data
    Given I open "https://demoqa.com/automation-practice-form" page
    When I fill the form with valid data
    Then I see the registration success message