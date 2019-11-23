import pytest
import os
import urllib.request

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#def driver_get(request):

#Initialise ChromeDriver
driver=webdriver.Chrome()

#def test_login(browser):

driver.maximize_window()

#Test case 1.0: Access login page

driver.get('http://127.0.0.1:8000/admin')


#Test case 1.1: Failed login in website

username="iamnotregistered"
password="notregistered"
driver.find_element_by_id("id_username").send_keys(username)
driver.find_element_by_id ("id_password").send_keys(password)
driver.find_element_by_css_selector("input[type='submit'][value='Log in']").click()
driver.find_element_by_id("id_username").clear()
driver.find_element_by_id("id_password").clear()

#Test case 1.2: Successful login to website as staff

username="staff1"
password="staffonly"
driver.find_element_by_id("id_username").send_keys(username)
driver.find_element_by_id ("id_password").send_keys(password)
driver.implicitly_wait(3)
driver.find_element_by_css_selector("input[type='submit'][value='Log in']").click()
assert "Django" in driver.title
driver.find_element_by_xpath('//div[@id="user-tools"]//a[.= "Log out"]').click()
driver.implicitly_wait(3)
driver.find_element_by_xpath('//div[@id="content"]//a[.= "Log in again"]').click()
driver.implicitly_wait(3)

#Test case 1.3: Successful login to website as admin

username="admin"
password="admin1234!"
driver.find_element_by_id("id_username").send_keys(username)
driver.find_element_by_id ("id_password").send_keys(password)
driver.find_element_by_css_selector("input[type='submit'][value='Log in']").click()
assert "Django" in driver.title


#Test case 2.0: View homepage
driver.find_element_by_xpath('//div[@id="user-tools"]//a[.= "View site"]').click()

url="http://127.0.0.1:8000/projects"
driver.get(url)
#assert "Projects" in driver.title


#Test case 3.0: View blog
driver.find_element_by_xpath('//div[@id="navbarSupportedContent"]//a[.= "Blog"]').click()










