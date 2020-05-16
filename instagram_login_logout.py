#log in an log out of instagram

# Modules to be imported.
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#log_in details
user_name="USER NAME"
password="PASSWORD"

#INSTAGRAM URL
URL="https://www.instagram.com/?hl=en"
# Browser : Firefox.
driver=webdriver.Firefox(executable_path="PARTH TO geckodriver")
driver.get(URL)
time.sleep(3)

#log In
driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input').send_keys(user_name)
time.sleep(5)
driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input').send_keys(password)
time.sleep(5)
driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]/button').click()
time.sleep(5)
driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]').click()
time.sleep(5)

#logout 
driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/a/img').click()
time.sleep(5)
driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/div[1]/div/button').click()
time.sleep(3)
driver.find_element_by_xpath('/html/body/div[4]/div/div/div/button[9]').click()
time.sleep(5)

#Exit browser
driver.quit()