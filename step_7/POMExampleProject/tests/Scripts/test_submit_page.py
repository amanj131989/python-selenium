from src.TestBase.WebDriverSetup import WebDriverSetup
from src.PageObject.Pages.SubmitPage import Submit

from tests.Scripts import project_urls
import time
import unittest

class SubmitTestCase(WebDriverSetup):

    def test_web_form(self):
        driver = self.driver
        self.driver.get(project_urls.submit_page)
        self.driver.set_page_load_timeout(30)

        web_page_title = "Web form - target page"

        try:
            if driver.title == web_page_title:
                print("WebPage loaded successfully")
                self.assertEqual(driver.title, web_page_title)
        except Exception as error:
            print(error + "WebPage Failed to load")

        # Create an instance of the class so that you we can make use of the methods
        # in the class
        submit = Submit(driver)
        time.sleep(2)
        self.assertEqual("Received!", submit.received_text.text)


if __name__ == '__main__':
    unittest.main()
