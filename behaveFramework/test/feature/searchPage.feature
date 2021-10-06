Feature: Search engine in browser
  Scenario: Search words in search engine in different browser
    Given Open 'google' in 'chrome'
    Then search for 'Lord Shiva'
