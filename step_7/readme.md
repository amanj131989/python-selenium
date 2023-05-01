# Lets learn Page Object Model and implement it with an example

The folder structire should be as below: 

+ Project-Directory
  + src
    + PageObject
      + Pages
        + *Page.py (Implementation of methods that make use of the respective Locators declared in Locators.py)
    + TestBase
      + WebDriverSetup.py
  + tests
    + Scripts
      + test_*.py (Implementation of test code)(There should be 1:1 mapping of *Page.py and test_*.py as it helps in making the code more modular)
    + TestSuite
      + TestRunner.py (contains TestSuite, which is a collection of test cases)
