from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

import unittest
import time


class NonPOMTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("https://www.selenium.dev/selenium/web/web-form.html")

    def test_my_text(self):
        driver = self.driver

        # Perform search operation
        elem = driver.find_element(By.NAME, "my-text")
        elem.send_keys("Hello Students")
        time.sleep(4)
        elem.submit()

    def tearDown(self):
        # Close the browser.
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
