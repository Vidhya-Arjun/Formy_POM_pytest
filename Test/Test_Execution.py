import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from Utils.conftest import *

def test_form_automation(setup_browser):
    driver = setup_browser
    driver.find_element(By.ID,"first-name").send_keys("John")
    driver.find_element(By.ID,"last-name").send_keys("Doe")
    driver.find_element(By.ID,"job-title").send_keys("Test")
    driver.find_element(By.XPATH,"//input[@id='radio-button-3']").click()
    driver.find_element(By.XPATH,"//div[contains(normalize-space(),'Male')]//input[@id='checkbox-1']").click()
    dropdown = driver.find_element(By.ID,"select-menu")
    select = Select(dropdown)
    select.select_by_index(2)
    driver.find_element(By.ID,"datepicker").send_keys("2026-03-31")
    driver.find_element(By.XPATH,"//a[@role='button']").click()
    time.sleep(1)
    wait = WebDriverWait(driver, 10)
    success_message = wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//h1"))).text
    assert success_message == "Thanks for submitting your form"