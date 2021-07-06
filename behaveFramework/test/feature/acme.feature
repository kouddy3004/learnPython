Feature: Validate ACME Demo setup
  Background: Login into Acme URL
    Given Login with UserName and Password


  Scenario: Validate Data available in Home Page
    When Fetch values from UI
    When Fetch values from Database
    Then Validate values from UI and Database


