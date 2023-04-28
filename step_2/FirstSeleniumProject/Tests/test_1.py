# Eight Basic Components
# 1. Start the session:

# Read example of your browser here, based on selenium version https://github.com/SergeyPirogov/webdriver_manager
# I am using Edge, selenium 4

from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

# 2. Take action on browser. Such as navigate to, 
driver.get("https://www.selenium.dev/selenium/web/web-form.html")

# 3. Request browser information.
# There are a bunch of types of information about the browser you can request, 
# including window handles, browser size / position, cookies, alerts, etc.
title = driver.title

# 4. Establish Waiting Strategy
# You want to make sure that the element is on the page before you attempt to locate it 
# and the element is in an interactable state before you attempt to interact with it.
# different strategies at https://www.selenium.dev/documentation/webdriver/waits/
# useful when certain elements on the webpage are not available immediately and need some time to load
driver.implicitly_wait(0.5)

# 5. Find an element 
from selenium.webdriver.common.by import By

text_box = driver.find_element(by=By.Name, value="my-text")
submit_buttom = driver.find_element(by=By.CSS_SELECTOR, value="button")

# 6. Take action on element (only 5 = click, send keys, clear, submit, select)
text_box.send_keys("Selenium")
submit_button.click()

# 7. Request element information 
# Elements store a lot of information that can be requested. 
# https://www.selenium.dev/documentation/webdriver/elements/information/
value = message.text

# 8. End the session
# This ends the driver process, which by default closes the browser as well. 
# No more commands can be sent to this driver instance.
# close() closes only the current window on which Selenium is running automated tests. 
# The WebDriver session, however, remains active. On the other hand, the driver. 
# quit() method closes all browser windows and ends the WebDriver session.
driver.quit()
