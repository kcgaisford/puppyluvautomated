import os
from selenium import webdriver

# Gets current working directory -> this is used for the ChromeDriver execable.
filepath = os.getcwd()

# Resuable function that allows us to get the attributes of Selenium elements
def get_attrs(element):
    # Thanks Alecxe -> https://stackoverflow.com/questions/27307131/selenium-webdriver-how-do-i-find-all-of-an-elements-attributes
    attrs = driver.execute_script('var items = {}; for (index = 0; index < arguments[0].attributes.length; ++index) { items[arguments[0].attributes[index].name] = arguments[0].attributes[index].value }; return items;', element)
    return attrs

# Finds a class located on a button and clicks it. In our example the buttons were red. 
def red_btn_click(red):
    # red button on the Home page
    red_btn = driver.find_element_by_css_selector(f"button.{red}")
    # found the button now CLICK
    red_btn.click()


# Sets browser to Chrome -> You can download Chrome driver from here: https://chromedriver.chromium.org/
driver = webdriver.Chrome(executable_path=f"{filepath}/chromedriver")
# Goes to a webpage
driver.get("http://localhost:3000/")

red_btn_click("red-color")

# Find all the red buttons and loop through them as "current_btn"
for current_btn in driver.find_elements_by_css_selector("button.bg-red-600"):
    # Just a reminder that this ------^ is elements with a 'S' for multiple elements
    # Calls our Attribute class defined above
    attrs = get_attrs(current_btn)
    if attrs['data-event-title'] == 'Husky':
        current_btn.click()
        # Below are finding elements by ID don't for get about the .send_keys()
        driver.find_element_by_id('name').send_keys("Kris")
        driver.find_element_by_id('email').send_keys("email@emailserver.com")
        driver.find_element_by_id('number').send_keys("2")
        red_btn_click("bg-red-600")




# Close Chrome
# driver.close()
