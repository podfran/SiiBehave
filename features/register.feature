Feature: Register on website

  Scenario: Register with valid email address
    Given a web browser is on the Sii store registration page
    When valid details are entered
    Then the user is logged in