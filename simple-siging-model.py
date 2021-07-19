from selenium import webdriver
import time

path ="chromedriver.exe"

driver = webdriver.Chrome(path)
driver.get("http://kennethhutw.github.io/demo/Selenium/Signin.html")
driver.find_element_by_id('password').clear()
driver.refresh()

driver.find_element_by_id('username').send_keys('kenneth')
time.sleep(2)
driver.find_element_by_id('password').send_keys('password')
time.sleep(2)
driver.find_element_by_id('dashboard').click()
time.sleep(2)
driver.find_element_by_id('Signin').click()
time.sleep(2)

username = driver.find_element_by_xpath('//*[@id="username"]')
print('user : ' + username.text + ' login successfully! ')
time.sleep(2)
print('Pass!!')