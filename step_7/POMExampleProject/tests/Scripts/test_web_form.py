from src.TestBase.WebDriverSetup import WebDriverSetup
from src.PageObject.Pages.WebFormPage import WebForm

from tests.Scripts import project_urls

import unittest
import time


class WebFormTestCase(WebDriverSetup):

    def test_web_form(self):
        driver = self.driver
        self.driver.get(project_urls.web_form)
        self.driver.set_page_load_timeout(30)

        web_page_title = "Web form"

        try:
            if driver.title == web_page_title:
                print("WebPage loaded successfully")
                self.assertEqual(driver.title, web_page_title)
        except Exception as error:
            print(error + "WebPage Failed to load")

        # Create an instance of the class so that you we can make use of the methods
        # in the class
        home_page = WebForm(driver)
        home_page.text_input.send_keys("From POM Demo")
        time.sleep(2)
        home_page.select_dropdown.select_by_visible_text("Two")
        time.sleep(2)
        home_page.submit_button.submit()
        time.sleep(2)
        print(driver.current_url)
        self.assertEqual(driver.current_url, project_urls.submit_page)


if __name__ == '__main__':
    unittest.main()
