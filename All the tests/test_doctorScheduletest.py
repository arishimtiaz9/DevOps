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

class TestDoctorScheduletest():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_doctorScheduletest(self):
    self.driver.get("http://localhost:8081/PHP-Doctor-Appointment-System/index.php")
    self.driver.set_window_size(1382, 744)
    self.driver.find_element(By.LINK_TEXT, "Doctor\'s Portal").click()
    self.driver.find_element(By.NAME, "doctorId").click()
    self.driver.find_element(By.NAME, "doctorId").send_keys("123")
    self.driver.find_element(By.NAME, "password").send_keys("123")
    self.driver.find_element(By.NAME, "login").click()
    self.driver.find_element(By.LINK_TEXT, "Doctor Schedule").click()
    self.driver.execute_script("window.scrollTo(0,215)")
    self.driver.find_element(By.ID, "date").click()
    self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(3) > .day:nth-child(6)").click()
    self.driver.find_element(By.NAME, "submit").click()
    element = self.driver.find_element(By.NAME, "submit")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, ".clockpicker-hours > .clockpicker-tick:nth-child(1)")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).click_and_hold().perform()
    element = self.driver.find_element(By.CSS_SELECTOR, ".clockpicker-canvas-fg")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).release().perform()
    self.driver.find_element(By.CSS_SELECTOR, ".clockpicker-plate").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".clockpicker-minutes > .clockpicker-tick:nth-child(1)")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).click_and_hold().perform()
    element = self.driver.find_element(By.CSS_SELECTOR, ".clockpicker-canvas-fg")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).release().perform()
    self.driver.find_element(By.CSS_SELECTOR, ".clockpicker-plate").click()
    self.driver.find_element(By.NAME, "submit").click()
    element = self.driver.find_element(By.NAME, "submit")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, ".clockpicker-dial:nth-child(1) > .clockpicker-tick:nth-child(24)")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).click_and_hold().perform()
    element = self.driver.find_element(By.CSS_SELECTOR, ".clockpicker-canvas:nth-child(3) .clockpicker-canvas-fg")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).release().perform()
    self.driver.find_element(By.CSS_SELECTOR, ".popover:nth-child(18) .clockpicker-plate").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".clockpicker-minutes:nth-child(2) > .clockpicker-tick:nth-child(12)")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).click_and_hold().perform()
    element = self.driver.find_element(By.CSS_SELECTOR, ".clockpicker-canvas:nth-child(3) .clockpicker-canvas-fg")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).release().perform()
    self.driver.find_element(By.CSS_SELECTOR, ".popover:nth-child(18) .clockpicker-plate").click()
    self.driver.find_element(By.NAME, "submit").click()
  