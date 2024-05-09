# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestPatientList():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_patientList(self):
    self.driver.get("http://localhost:8080/")
    self.driver.set_window_size(1382, 744)
    self.driver.find_element(By.LINK_TEXT, "Doctor\'s Portal").click()
    self.driver.find_element(By.NAME, "doctorId").click()
    self.driver.find_element(By.NAME, "doctorId").send_keys("123")
    self.driver.find_element(By.NAME, "password").send_keys("123")
    self.driver.find_element(By.NAME, "password").send_keys(Keys.ENTER)
    self.driver.find_element(By.LINK_TEXT, "Patient List").click()
    self.driver.find_element(By.LINK_TEXT, "Doctor Rishi").click()
    self.driver.find_element(By.LINK_TEXT, "Log Out").click()
  
