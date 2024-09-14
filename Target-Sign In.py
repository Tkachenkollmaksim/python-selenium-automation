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

driver.get('https://www.target.com/')

#Click Sign-In
driver.find_element(By.XPATH, value="//a[@data-test='@web/AccountLink']").click()

sleep(6)

driver.find_element(By.XPATH, value="//a[@data-test='accountNav-signIn']").click()
sleep(6)

#Verification
actual_result = driver.find_element(By. XPATH, value="//h1[@class='sc-fe064f5c-0 sc-315b8ab9-2 WObnm gClYfs']").text
expected_result = 'Sign Off'
sleep(6)

assert expected_result in actual_result, f'Expected {expected_result}, got actual {actual_result}'

print('Target Test Complete')

driver.quit()