# Help: https://selenium-python.readthedocs.io/locating-elements.html

# 1. Selenium provides following two methods
# get_element (returns first match)
# get_elements (returns a list)
# If no element has a matching attribute, a NoSuchElementException will be raised

# 2. By Class is used to specify which attribute is used to locate elements
find_element(By.ID, "id")
find_element(By.NAME, "name")
find_element(By.XPATH, "xpath")
find_element(By.LINK_TEXT, "link text")
find_element(By.PARTIAL_LINK_TEXT, "partial link text")
find_element(By.TAG_NAME, "tag name")
find_element(By.CLASS_NAME, "class name")
find_element(By.CSS_SELECTOR, "css selector")

# Use https://www.selenium.dev/selenium/web/web-form.html
# 3.1 By.ID
my_text = driver.find_element(By.ID, 'my-text-id')

# 3.2 By.NAME
my_text = driver.find_element(By.NAME, 'my-text')

# 3.3. By.XPATH
# <html>
#  <body>
#   <form id="loginForm">
#    <input name="username" type="text" />
#    <input name="password" type="password" />
#    <input name="continue" type="submit" value="Login" />
#    <input name="continue" type="button" value="Clear" />
#   </form>
# </body>
# </html>
# Consider above HTML

# Absolute path (would break if the HTML was changed only slightly)
# note indexing starts with 1 in XPath
login_form = driver.find_element(By.XPATH, "/html/body/form[1]")

# First form element in the HTML
# note indexing starts with 1 in XPath
login_form = driver.find_element(By.XPATH, "//form[1]")

# The form element with attribute id set to loginForm
login_form = driver.find_element(By.XPATH, "//form[@id='loginForm']")

# First form element with an input child element with name set to username
username = driver.find_element(By.XPATH, "//form[input/@name='username']")

# First input child element of the form element with attribute id set to loginForm
username = driver.find_element(By.XPATH, "//form[@id='loginForm']/input[1]")

# First input element with attribute name set to username
username = driver.find_element(By.XPATH, "//input[@name='username']")

# Input with attribute name set to continue and attribute type set to button
clear_button = driver.find_element(By.XPATH, "//input[@name='continue'][@type='button']")

# Fourth input child element of the form element with attribute id set to loginForm
clear_button = driver.find_element(By.XPATH, "//form[@id='loginForm']/input[4]")


# 3.4 Locating Hyperlinks by Link Text
# <html>
#  <body>
#   <p>Are you sure you want to do this?</p>
#   <a href="continue.html">Continue</a>
#   <a href="cancel.html">Cancel</a>
# </body>
# </html>

continue_link = driver.find_element(By.LINK_TEXT, 'Continue')
continue_link = driver.find_element(By.PARTIAL_LINK_TEXT, 'Conti')

# 3.5. Locating Elements by Tag Name
# <html>
#  <body>
#   <h1>Welcome</h1>
#   <p>Site content goes here.</p>
# </body>
# </html>
heading1 = driver.find_element(By.TAG_NAME, 'h1')

# 3.6. Locating Elements by Class Name
# <html>
#  <body>
#   <p class="content">Site content goes here.</p>
# </body>
# </html>
content = driver.find_element(By.CLASS_NAME, 'content')

# 3.7. Locating Elements by CSS Selectors
# Use this when you want to locate an element using CSS selector syntax
content = driver.find_element(By.CSS_SELECTOR, 'p.content')
