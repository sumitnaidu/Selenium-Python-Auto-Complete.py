from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
import unittest

class MyFirstCase():

 def __init__(self):
     driver = self.driver

 def setUp(self):
     driver = webdriver.Chrome("C:\\Users\\user\\Downloads\\chromedriver_win32\\chromedriver.exe")
     driver.get("https://www.google.co.in/")

 def test_autosuggestTest(self):
  try:
     driver = self.driver
     driver.find_element_by_name("q").send_keys("man")
     driver.implicitly_wait(3)
     auto_suggest = driver.find_elements_by_xpath(".//*[@class='sbsb_b']/li//div[2]")
    for items in auto_suggest :
          if  items.text == 'mangalore':
              items.click()

  except StaleElementReferenceException :
             pass

 def tearDown(self):
      self.driver.quit()