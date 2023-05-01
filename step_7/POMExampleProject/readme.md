This is the main project folder: It should have this two folder structure:
+ src
+ Project-Directory
     |--------- Src
                    |--------- PageObject
                                       |--------- Pages
                                                    |--------- *Page.py (Implementation of methods that make use of the respective Locators declared in Locators.py) 
                                       |--------- Locators.py
                    |--------- TestBase
                                       |--------- WebDriverSetup.py
     |--------- Test
                    |--------- Scripts
                                       |--------- test_*.py (Implementation of test code)(There should be 1:1 mapping of *Page.py and test_*.py as it helps in making the code more modular)
                    |--------- TestSuite
                                       |--------- TestRunner.py (contains TestSuite, which is a collection of test cases)
+ tests
