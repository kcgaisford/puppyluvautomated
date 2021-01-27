import os
from selenium import webdriver

filepath = os.getcwd()

def get_attrs(element):
    attrs = driver.execute_script('var items = {}; for (index = 0; index < arguments[0].attributes.length; ++index) { items[arguments[0].attributes[index].name] = arguments[0].attributes[index].value }; return items;', element)
    return attrs

def red_btn_click(red):
    # red button on the Home page
    red_btn = driver.find_element_by_css_selector(f"button.{red}")
    # found the button now CLICK
    red_btn.click()


# Sets browser to Chrome
driver = webdriver.Chrome(executable_path=f"{filepath}/chromedriver")
# Goes to a webpage
driver.get("http://localhost:3000/")

red_btn_click("red-color")

# Find all the red buttons and loop through them
for current_btn in driver.find_elements_by_css_selector("button.bg-red-600"):
    attrs = get_attrs(current_btn)
    if attrs['data-event-title'] == 'Husky':
        current_btn.click()
        driver.find_element_by_id('name').send_keys("Kris")
        driver.find_element_by_id('email').send_keys("email@emailserver.com")
        driver.find_element_by_id('number').send_keys("2")
        red_btn_click("bg-red-600")




# Close Chrome
# driver.close()