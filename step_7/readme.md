# Lets learn Page Object Model and implement it with an example

Why?
+ As software size increases, the complexity of the development code and the test code increases.
+ A proper project structure must be followed when developing automation test code; else, the code might become unmanageable.

Goals?
+ Reduce code duplication.
+ Minimize the efforts involved in code update/maintenance.

How are the goals acheived?
+ Make the code more modular.
  + Locators/elements used by the test suites/test scenarios are stored in a separate class file.
  + The test cases(that contain the core test logic) are in a different file.

Two crucial elements:
+ Page Object Element (Page Class/Page Object): An object repository for
  + the WebElements/Web UI Elements of the web-pages under test.
  + implementation of the interfaces/methods to perform operations on these web elements.
+ Test Cases:
  + Test cases contain the implementation of the actual test scenarios.
  + It uses page methods/methods in the page class to interact with the page’s UI elements.
  + If there is a change in the UI of the web page, only the Page Class needs to be updated, and the test code remains unchanged.

Advantages Of Page Object Model
+ Increased Reusability
+ Improved Maintainability
+ Minimal impact due to UI changes

Steps:
+ Start with `non_pom.py` file, and we will convert it to POM.

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
