Feature: Purchasing items

  @wip
  Scenario: Add item to cart
    Given a web browser is at the home page
    And no items are in cart
    When item from popular products is chosen
    And item is added to cart
    Then cart count increases
