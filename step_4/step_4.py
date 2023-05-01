# We will learn interactions in this step
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

driver.get("https://www.selenium.dev/selenium/web/web-form.html")

## Get browser information
print(driver.title)
print(driver.current_url)

## Browser navigation
# Navigate to
driver.get("https://www.selenium.dev/selenium/web/web-form.html")
# Back, press back button
driver.back()

# Forward, press forward button
driver.forward()

# Refresh, Refresh the current page:
driver.refresh()

## Alerts example
driver.get("https://www.selenium.dev/documentation/webdriver/interactions/alerts/")
# Click the link to activate the alert
driver.find_element(By.LINK_TEXT, "See an example alert").click()
# Wait for the alert to be displayed and store it in a variable
wait = WebDriverWait(driver, 5)
alert = wait.until(expected_conditions.alert_is_present())
# Store the alert text in a variable
text = alert.text
time.sleep(2)
# Press the OK button
alert.accept()

## Working with cookies
# A cookie is a small piece of data that is sent from a website and stored in your computer.
# Cookies are mostly used to recognise the user and load the stored information.
driver.add_cookie({"name": "Selenium", "value": "Unknown"})
# Cookies SameSite, Lax vs Strict
# to prevent CSRF https://spanning.com/wp-content/uploads/2019/04/cross-site-request-forgery-example.png
print(driver.get_cookies())

# Selenium code links: https://www.selenium.dev/selenium/docs/api/py/index.html
driver.quit()
