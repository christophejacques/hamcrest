# file:datatype.features/cardinality.zero_or_one.feature
Feature: Data Type with Cardinality 0..1 (Optional Part)

  Scenario: Case1 "When attacked by a ..."
    Given the ninja has a black-belt
    When attacked by a samurai
    Then the ninja should engage the opponent

  Scenario: Case2 "When attacked by ..."
    Given the ninja has a black-belt
    When attacked by Chuck Norris
    Then the ninja should run for his life

# -- DESCRIPTION:
# "When attacked by ...": Once with "a ", once without it.
# Only one step should be used.
