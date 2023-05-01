# We will learn interactions in this step
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

driver.get("file:///C:/Users/AJiddewar/Downloads/waits_demo.html")


# developer instructs driver to get element! but the element is not yet created! i.e race condition
# this is because of default page load strategy of webdriver
# https://www.selenium.dev/documentation/webdriver/drivers/options/#pageloadstrategy

# This is an example of explicit wait, until certain condition is satisfied!
# def document_initialised(driver):
#     return driver.execute_script("return initialised")
# WebDriverWait(driver, timeout=5).until(document_initialised)

el = driver.find_element(By.TAG_NAME, "p")
assert el.text == "Hello from JavaScript!"


driver.quit()
print("Run is complete!")
