# file:features/parse_matcher.feature
Feature: parse_matcher feature

Scenario: Run a simple test
    Given I use the regular expression step matcher
    Then the parameter "variable1" is "valeur1"
    Then the parameter "variable2" is none