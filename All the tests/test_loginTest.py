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

class TestLoginTest():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_loginTest(self):
    self.driver.get("http://localhost:8081/PHP-Doctor-Appointment-System/index.php")
    self.driver.set_window_size(1382, 744)
    self.driver.find_element(By.LINK_TEXT, "Login").click()
    self.driver.find_element(By.NAME, "icPatient").click()
    self.driver.find_element(By.NAME, "icPatient").send_keys("12345")
    self.driver.find_element(By.NAME, "password").click()
    self.driver.find_element(By.NAME, "password").send_keys("123")
    self.driver.find_element(By.ID, "login").click()
  
