from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url of web
driver.get('https://www.amazon.com/ap/register?showRememberMe=true&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_ya_signin&prevRID=J1F7KK9T91EERPC3AX88&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&prepopulatedLoginId=&failedSignInCount=0&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&pageId=usflex&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0')

#Amazon Logo
driver.find_element(By.CSS_SELECTOR, value='.a-icon.a-icon-logo')

#Create Account
driver.find_element(By.CSS_SELECTOR, value='.a-spacing-small')

#Your name
driver.find_element(By.CSS_SELECTOR, "[placeholder='First and last name']")

#Your Email/Number
driver.find_element(By.ID, value="ap_email")

#Your Password
driver.find_element(By.ID, value="ap_password")

#Your Re-enter Password
driver.find_element(By.ID, value='ap_password_check')

#Continue Button
driver.find_element(By.ID, value='continue')

#Condition of Use
driver.find_element(By.CSS_SELECTOR, "#legalTextRow [href*='Conditions of Use']")

#Privacy Notice
driver.find_element(By.CSS_SELECTOR, "#legalTextRow [href*='Privacy Notice']")

#Sign In
driver.find_element(By.CSS_SELECTOR, value='.a-link-emphasis')


sleep(6)

print('test passed')
