import pytest
import os
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


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
time.sleep(3)
driver.find_element_by_id("id_username").clear()
driver.find_element_by_id("id_password").clear()

#Test case 1.2: Successful login to website as staff

username="staff1"
password="staffonly"
driver.find_element_by_id("id_username").send_keys(username)
driver.find_element_by_id ("id_password").send_keys(password)
driver.find_element_by_css_selector("input[type='submit'][value='Log in']").click()
assert "Django" in driver.title
driver.find_element_by_xpath('//div[@id="user-tools"]//a[.="Log out"]').click()
time.sleep(3)
driver.find_element_by_xpath('//div[@id="content"]//a[.="Log in again"]').click()
time.sleep(3)

#Test case 1.3: Successful login to website as admin

username="admin"
password="admin1234!"
driver.find_element_by_id("id_username").send_keys(username)
driver.find_element_by_id ("id_password").send_keys(password)
time.sleep(3)
driver.find_element_by_css_selector("input[type='submit'][value='Log in']").click()
time.sleep(3)
assert "Django" in driver.title


#Test case 2.0: View homepage
driver.find_element_by_xpath('//div[@id="user-tools"]//a[.= "View site"]').click()
url="http://127.0.0.1:8000/projects"
driver.get(url)
#assert "Projects" in driver.title


#Test case 3.0: View blog
driver.find_element_by_xpath('//div[@id="navbarSupportedContent"]//a[.= "Blog"]').click()
#assert "Home" in driver.title


#Test case 4.0: View project
driver.find_element_by_xpath('//div[@id="navbarSupportedContent"]//a[.= "Blog"]').click()
time.sleep(3)
driver.execute_script("window.scrollTo(0, 2000)")
time.sleep(3)
#assert "Projects" in driver.title


#Test case 5.1: Post blog as admin
driver.get('http://127.0.0.1:8000/admin')
#driver.FindElement(By.XPath("//tr[contains(., 'model-user')]/td[1]//input[@type='link']")).Click();
driver.get('http://127.0.0.1:8000/admin/blog/post/add/')
#assert "Add post" in driver.titles


#Test case 5.2: Admin inputs nothing in blog
error_msg="Please correct the errors below."
title=""
body=""
driver.find_element_by_name("title").send_keys(title)
driver.find_element_by_name("body").send_keys(body)
el = driver.find_element_by_id('post_form')
for option in el.find_elements_by_id('id_categories'):
    if option.text == 'Category object (1)':
        option.click() # select() in earlier versions of webdriver
        break
time.sleep(3)
driver.find_element_by_css_selector("input[type='submit'][value='Save']").click()
actual_msg=driver.find_element_by_name('csrfmiddlewaretoken').text
#assertTrue(actual_msg.contains(error_msg))
time.sleep(3)


#Test case 5.3: Admin inputs test post
title="Test"
body="Test"
driver.find_element_by_name("title").send_keys(title)
driver.find_element_by_name("body").send_keys(body)
el = driver.find_element_by_id('post_form')
for option in el.find_elements_by_id('id_categories'):
    if option.text == 'Category object (1)':
        option.click() # select() in earlier versions of webdriver
        break
#assert "Select post to change | Django site admin" in driver.title
driver.get('http://127.0.0.1:8000/blog')
driver.execute_script("window.scrollTo(0, 3000)")
time.sleep(3)



#Test case 5.0 & 6.0: Post blog as staff & User not registered as admin

error_msg="You don't have permission to view or edit anything."
driver.get('http://127.0.0.1:8000/admin')
driver.find_element_by_xpath('//div[@id="user-tools"]//a[.="Log out"]').click()
time.sleep(3)
driver.find_element_by_xpath('//div[@id="content"]//a[.="Log in again"]').click()
time.sleep(3)
username="staff1"
password="staffonly"
driver.find_element_by_id("id_username").send_keys(username)
driver.find_element_by_id ("id_password").send_keys(password)
time.sleep(3)
driver.find_element_by_css_selector("input[type='submit'][value='Log in']").click()
time.sleep(3)
actual_msg=driver.find_element_by_id("content-main").text;
assert actual_msg==error_msg
driver.find_element_by_xpath('//div[@id="user-tools"]//a[.="Log out"]').click()
time.sleep(3)
driver.find_element_by_xpath('//div[@id="content"]//a[.="Log in again"]').click()
time.sleep(3)


#Test case 6.1: View list of registered users as admin
username="admin"
password="admin1234!"
driver.find_element_by_id("id_username").send_keys(username)
driver.find_element_by_id ("id_password").send_keys(password)
time.sleep(3)
driver.find_element_by_css_selector("input[type='submit'][value='Log in']").click()
time.sleep(3)
#driver.FindElement(By.XPath("//tr[contains(., 'model-group')]/td[1]//input[@type='link']")).Click();
driver.get('http://127.0.0.1:8000/admin/auth/user/')
time.sleep(3)
assert "Select user to change | Django site admin" in driver.title
driver.find_element_by_xpath('//div[@id="user-tools"]//a[.="Log out"]').click()
time.sleep(3)
driver.find_element_by_xpath('//div[@id="content"]//a[.="Log in again"]').click()
time.sleep(3)

#The end
driver.quit()





