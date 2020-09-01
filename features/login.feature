Feature: Login to website

  Scenario: Login as existing user
    Given a web browser is at the Sii store login page
    When registered credentials are used
    Then the user is logged in