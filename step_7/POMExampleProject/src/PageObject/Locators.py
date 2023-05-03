
class Locator(object):

    # XPath Tutorial: http://www.zvon.org/comp/r/tut-XPath_1.html#intro

    # For WebFrom
    text_input = "//input[@name='my-text']"
    select_dropdown = "//select[@class='form-select']"
    submit_button = "//button[@type='submit']"

    # For SubmitPage
    received_text = "//p[@id='message']"
