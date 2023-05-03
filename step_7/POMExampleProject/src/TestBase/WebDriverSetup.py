import unittest
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from selenium import webdriver


class WebDriverSetup(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def tearDown(self):
        if self.driver:
            print("Cleanup of test environment")
            self.driver.close()
            self.driver.quit()
