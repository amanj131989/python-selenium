from selenium.webdriver.common.by import By
from src.PageObject.Locators import Locator
from selenium.webdriver.support.ui import Select


class WebForm(object):
    def __init__(self, driver):
        self.driver = driver
        self.text_input = driver.find_element(By.XPATH, Locator.text_input)
        self.select_dropdown = Select(driver.find_element(By.XPATH, Locator.select_dropdown))
        self.submit_button = driver.find_element(By.XPATH, Locator.submit_button)

    def getTextInput(self):
        return self.text_input

    def getSelectDropdown(self):
        return self.select_dropdown

    def getSubmitButton(self):
        return self.submit_button

