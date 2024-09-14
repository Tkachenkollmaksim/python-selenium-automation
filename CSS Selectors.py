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

# open the url
driver.get('https://www.amazon.com/')

#By CSS, by class
driver.find_element(By.CSS_SELECTOR, value='.nav-progressive-attribute')
driver.find_element(By.CSS_SELECTOR, value='.nav-input.nav-progressive-attribute')
#By CSS, by class(es)
driver.find_element(By.CSS_SELECTOR, value='input.nav-input.nav-progressive-attribute')
#By CSS, by ID & class
driver.find_element(By.CSS_SELECTOR, value='input#twotabseatchtextbox.nav-input.nav-progressive-attribute')
#By CSS, attributes
driver.find_element(By.CSS_SELECTOR, value="[name='field-keywords']")
driver.find_element(By.CSS_SELECTOR, value="input[name='field-keywords']")
driver.find_element(By.CSS_SELECTOR, value=".nav-input[tabindex='0'][name='field-keywords']")
#By CSS, attribute, ,partial match
driver.find_element(By.CSS_SELECTOR, value="[href*='notification_condition_of_use']")
driver.find_element(By.CSS_SELECTOR, value="[class*='input']")
driver.find_element(By.CSS_SELECTOR, value="[id*='input']")

#By CSS, parent =>Child separate by Space
driver.find_element(By.CSS_SELECTOR, value="#legalTextRow [href*='privacy']")


