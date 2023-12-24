# Imports stealth
from selenium_stealth import stealth
# Python's built in time module
import time
# Python's built-in random module
import random
# imports webdriver
from selenium import webdriver
# WebDriverWait waits for the element to be present on the page and acts upon it
from selenium.webdriver.support.wait import WebDriverWait
# Select is used for elements in the dropdown manu
from selenium.webdriver.support.ui import Select
# NoSuchElementException occurs when the element is not present to be selected
from selenium.common.exceptions import NoSuchElementException
# Defined conditions to use with WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# Selecting elements using By
from selenium.webdriver.common.by import By
# Keys is used to mimick key presses within Selenium
from selenium.webdriver.common.keys import Keys

opt = webdriver.ChromeOptions()
# Configurations for selenium driver
opt.add_experimental_option("excludeSwitches", ["enable-automation"])
opt.add_argument("--profile-directory=Person 4")
opt.add_experimental_option('useAutomationExtension', False)
opt.add_argument("disable-popup-blocking")
driver = webdriver.Chrome(options=opt)
# Calls and configure Selenium stealth using OpenGL
stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win64",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )
# put the link of product here in .get()
driver.get("https://digilog.pk/products/wemos-d1-mini-pro-external-antenna-wi-fi-antenna-in-pakistan?_pos=2&_sid=c257c8422&_ss=r")
foundButton = False
time.sleep(5)

# While loop looks for add to cart button and refreshes page until found

addToCartButton = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'ProductSubmitButton-template--21373722493206__main'))
    )
addToCartButton.click()


viewCart = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "cart-count-bubble"))
)
viewCart.click()

quantity = 3    #specify the  quantity of products

for i in range(quantity):
    plus = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.NAME, 'plus'))
    )
    plus.click()


time.sleep(5)
checkout = driver.find_element(By.ID, 'checkout')

# Click on the 'checkout' element
checkout.click()


phoneNumber = WebDriverWait(driver, 120).until(
    EC.element_to_be_clickable((By.NAME, "email")))


# Types in each character at a random interval, makes input more human-like
for i in "xyz@gmail.com":
    phoneNumber.send_keys(i)
    time.sleep(random.uniform(0, 0.5))


firstName = driver.find_element_by_name("firstName")
# Types in each character at a random interval, makes input more human-like
for i in "Hammad":
    firstName.send_keys(i)
    time.sleep(random.uniform(0, 0.5))
# Looks for last name field by searching for the element by name
lastName = driver.find_element_by_name("lastName")
# Types in each character at a random interval, makes input more human-like
for i in "hon yr":
    lastName.send_keys(i)
    time.sleep(random.uniform(0, 0.5))
time.sleep(1)






address = driver.find_element_by_name("address1")
# Types in each character at a random interval, makes input more human-like
for i in "adfds adsfds32 ddas":
    address.send_keys(i)
    time.sleep(random.uniform(0, 0.5))

city = driver.find_element_by_name("city")
# Types in each character at a random interval, makes input more human-like
for i in "Karachi":
    city.send_keys(i)
    time.sleep(random.uniform(0, 0.5))
time.sleep(1)

postalCode = driver.find_element_by_name("postalCode")
# Types in each character at a random interval, makes input more human-like
for i in "77000":
    postalCode.send_keys(i)
    time.sleep(random.uniform(0, 0.5))
time.sleep(1)


phone = driver.find_element_by_name("phone")
# Types in each character at a random interval, makes input more human-like
for i in "03423811921":
    phone.send_keys(i)
    time.sleep(random.uniform(0, 0.5))
time.sleep(1)



# Locate the Bank Transfer radio button by its ID
bank_transfer_radio = driver.find_element(By.ID, 'basic-customManualPayment-101159895318')

# Check if the radio button is not selected, and if not, select it
if not bank_transfer_radio.is_selected():
    bank_transfer_radio.click()
# Check if the radio button is not selected, and if not, select it

time.sleep(2)
completeOrderButton = driver.find_element(By.CLASS_NAME, 'QT4by')

# Click on the 'checkout' element
completeOrderButton.click()


# Types in each character at a random interval, makes input more human-like

loginPass = WebDriverWait(driver, 120).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "mod-input mod-input-password mod-login-input-password mod-input-password")))

# Types in each character at a random interval, makes input more human-like
for i in "enterpassword":     # enter the email adress here
    loginPass.send_keys(i)
    time.sleep(random.uniform(0, 0.5))


time.sleep(60)
# Quits driver
driver.quit()
