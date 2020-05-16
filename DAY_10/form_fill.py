# Modules to be imported.
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Your login details.
email = "18egjit002@gitjaipur.com"
passwd = "8dJ#J4wa"


# Browser : Firefox.
driver = webdriver.Firefox(executable_path="/Users/CHANDAN/geckodriver.exe")
driver.get("https:bit.ly/fssdp20assign")
time.sleep(1)

# GMAIL login.
driver.find_element_by_xpath('//*[@id="identifierId"]').send_keys(email)
time.sleep(1)
driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/span/span').click()
time.sleep(3)
driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input').send_keys(passwd)
time.sleep(1)
login=driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/span/span')
login.click()
time.sleep(1)
# filling form.
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[1]/div[2]/form/div/div/div[2]/div[1]/div[2]/div/div[1]/div/div[1]/input').send_keys(email)
driver.find_element_by_xpath('/html/body/div[1]/div[2]/form/div/div/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]/input').send_keys('CHANDAN KUMAR JANGID')
driver.find_element_by_xpath('/html/body/div[1]/div[2]/form/div/div/div[2]/div[3]/div/div[2]/div/span/div/div[1]/label/div/div[1]/div').click()
driver.find_element_by_xpath('/html/body/div[1]/div[2]/form/div/div/div[2]/div[4]/div/div[2]/div/div[1]/div/div[1]/input').send_keys('GIT Jaipur')
driver.find_element_by_xpath('/html/body/div[1]/div[2]/form/div/div/div[2]/div[5]/div/div[2]/div/div[1]/div/div[1]/input').send_keys('18EGJIT002')
driver.find_element_by_xpath('/html/body/div[1]/div[2]/form/div/div/div[2]/div[6]/div/div[2]/div/div[1]/div/div[1]/input').send_keys('8374837054')
driver.find_element_by_xpath('/html/body/div[1]/div[2]/form/div/div/div[2]/div[7]/div/div[2]/div/div[1]/div/div[1]/input').send_keys('DAY 10-SUBMITTING ASSIGNMENT USING AUTOMATION')
driver.find_element_by_xpath('/html/body/div[1]/div[2]/form/div/div/div[2]/div[8]/div/div[3]').click()
time.sleep(4)
iframe=driver.find_element_by_class_name('picker-frame')
driver.switch_to.frame(iframe);
driver.find_element_by_xpath('/html/body/div[2]/div/div[4]/div[2]/div/div[2]/div/div/div[1]/div/div[2]/div[1]/div/div/div[4]/div').click()
time.sleep(20)
driver.find_element_by_xpah('//*[@id="picker:ap:0"]').click()
time.sleep(5)

# Closing Browser.
#driver.quit()
