# Modules to be imported.
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Your login details.
email = "xyz.com"
passwd = "8dJeffww"

# Browser : Firefox.
driver = webdriver.Firefox(executable_path="/Users/CHANDAN/geckodriver.exe")
driver.get("https://accounts.google.com/ServiceLogin/identifier?service=mail&passive=true&rm=false&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
time.sleep(1)

# GMAIL login.
username=driver.find_element_by_xpath('//*[@id="identifierId"]')
username.send_keys(email)
time.sleep(1)
next=driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/span/span')
next.click()
time.sleep(1)
password=driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input')
password.send_keys(passwd)
time.sleep(1)
login=driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/span/span')
login.click()
time.sleep(5)
# GMAIL logout.
logout=driver.find_element_by_xpath('/html/body/div[7]/div[3]/div/div[1]/div[3]/header/div[2]/div[3]/div[1]/div[2]/div[2]/div/a')
logout.click()
time.sleep(2)
logout2=driver.find_element_by_xpath('//*[@id="gb_71"]')
logout2.click()
time.sleep(5)
# Closing Browser.
driver.quit()
