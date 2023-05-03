from selenium.webdriver.common.by import By
from src.PageObject.Locators import Locator


class Submit(object):
    def __init__(self, driver):
        self.driver = driver
        self.received_text = driver.find_element(By.XPATH, Locator.received_text)

    def getReceivedText(self):
        return self.received_text
