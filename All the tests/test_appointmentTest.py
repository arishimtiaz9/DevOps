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

class TestAppointmentTest():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_appointmentTest(self):
    self.driver.get("http://localhost:8081/PHP-Doctor-Appointment-System/patient/patient.php")
    self.driver.set_window_size(1936, 1056)
    self.driver.find_element(By.ID, "date").click()
    self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(3) > .day:nth-child(3)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
    self.driver.find_element(By.NAME, "symptom").click()
    self.driver.find_element(By.NAME, "symptom").send_keys("Fever")
    self.driver.find_element(By.NAME, "comment").click()
    self.driver.find_element(By.NAME, "comment").send_keys("Not well")
    self.driver.find_element(By.ID, "submit").click()
  